import jwt

jwt.encode({})

# Running this through mypy should produce the following error:
#
# error: Too few arguments for "encode"
