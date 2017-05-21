import os
import sys
import subprocess
from pathlib import Path
from typing import List

MY_DIR = Path(__file__).resolve().parent
GOOD_EXAMPLES_DIR = MY_DIR / 'good_examples'
BAD_EXAMPLES_DIR = MY_DIR / 'bad_examples'
MYPY_ENV = os.environ
MYPY_ENV['MYPYPATH'] = str(MY_DIR / 'mypy-stubs')

def make_mypy_args(path: Path) -> List[str]:
    return [
        sys.executable,
        '-m', 'mypy',
        str(path),
        '--strict',
        '--incremental',
    ]

print("Testing good examples...")

subprocess.check_call(make_mypy_args(GOOD_EXAMPLES_DIR), env=MYPY_ENV)

print("Testing bad examples...")

for pyfile in BAD_EXAMPLES_DIR.glob('**/*.py'):
    pyfile = pyfile.relative_to(Path.cwd())

    print(f"  Examining {pyfile}...")

    expected_output = pyfile.read_text().split('\n')[-2]
    if not expected_output.startswith('# '):
        raise Exception(f'Expected the last line of {pyfile} to be a comment')

    expected_output = expected_output[2:].strip()
    if not expected_output:
        raise Exception(f'Expected the last line of {pyfile} to contain '
                         'expected output')

    child = subprocess.run(make_mypy_args(pyfile), stdout=subprocess.PIPE,
                           env=MYPY_ENV)

    if child.returncode == 0:
        raise Exception(f'Expected {pyfile} to raise a mypy error')

    output = child.stdout.decode('utf-8')

    if expected_output not in output:
        raise Exception(f'Expected running mypy on {pyfile} to error '
                        f'with "{expected_output}", but it output '
                        f'"{output}"')

print("Tests pass!")
