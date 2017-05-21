import jwt

jwt.encode({15: '1'}, 'blah')

# Running this through mypy should produce the following error:
#
# error: Dict entry 0 has incompatible type "int": "str"
