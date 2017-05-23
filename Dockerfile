FROM python:3.6

COPY requirements.txt .

RUN pip install -r requirements.txt

# For some reason 'pip install cryptography' works but we still get
# 'ModuleNotFoundError: No module named Crypto', so we'll fall back
# to pycrypto/ecdsa.
RUN pip install pycrypto ecdsa

RUN pip install pyjwt
