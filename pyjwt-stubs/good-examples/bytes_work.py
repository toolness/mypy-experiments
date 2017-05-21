# These examples aren't from anywhere, but are based on my reading of
# the code.

import jwt

encoded = jwt.encode({}, b'blarg')

assert type(encoded) is bytes

decoded = jwt.decode(b'blarg')
