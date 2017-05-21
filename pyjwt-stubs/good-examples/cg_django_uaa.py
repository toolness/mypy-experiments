import jwt

access_token = jwt.encode({}, 'unused secret key (for verification)')

access_token.upper()  # Just make sure it has bytes methods.

user_info = jwt.decode('blarg', verify=False)

user_info.get('blah')  # Just make sure it has mapping keys that are strings.
