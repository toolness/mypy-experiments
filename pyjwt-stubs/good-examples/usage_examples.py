# Taken from https://pyjwt.readthedocs.io/en/latest/usage.html

import jwt
import datetime

encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})

jwt.decode(encoded, verify=False)

jwt.encode({'exp': 1371720939}, 'secret')
jwt.encode({'exp': datetime.datetime.utcnow()}, 'secret')

try:
    jwt.decode('JWT_STRING', 'secret')
except jwt.ExpiredSignatureError:
    # Signature has expired
    pass

jwt_payload = jwt.encode({
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
}, 'secret')

# JWT payload is now expired
# But with some leeway, it will still validate
jwt.decode(jwt_payload, 'secret', leeway=10)

jwt.decode(jwt_payload, 'secret', leeway=datetime.timedelta(seconds=10))

jwt.encode({'nbf': 1371720939}, 'secret')

jwt.encode({'nbf': datetime.datetime.utcnow()}, 'secret')

payload = {
    'some': 'payload',
    'iss': 'urn:foo'
}

token = jwt.encode(payload, 'secret')
decoded = jwt.decode(token, 'secret', issuer='urn:foo')

payload = {
    'some': 'payload',
    'aud': 'urn:foo'
}

token = jwt.encode(payload, 'secret')
decoded = jwt.decode(token, 'secret', audience='urn:foo')

jwt.encode({'iat': 1371720939}, 'secret')
jwt.encode({'iat': datetime.datetime.utcnow()}, 'secret')
