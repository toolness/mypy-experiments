# These are undocumented functions, but the package
# seems to export them in its root __init__.py, so we
# should at least make sure that mypy doesn't raise
# spurious errors if they're used.

import jwt

jwt.get_unverified_header
jwt.PyJWT
jwt.PyJWS
