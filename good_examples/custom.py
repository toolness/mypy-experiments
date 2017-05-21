import jwt

encoded = jwt.encode({}, b'blarg')

decoded = jwt.decode(b'blah')
