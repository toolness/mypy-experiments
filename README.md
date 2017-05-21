These are [mypy][] annotations for the [PyJWT][] library.

The annotations are in the `mypy-stubs` directory.

"Good" example code, which should pass strict type-checking, is
contained in the `good_examples` directory. Note that this code
*only* needs to pass strict type checking--it doesn't need to
actually execute without errors.

"Bad" example code, which should fail type-checking, is
contained in the `bad_examples` directory.

Run `python test.py` to ensure that the good and bad examples type-check
as expected.

[mypy]: http://www.mypy-lang.org/
[PyJWT]: https://github.com/jpadilla/pyjwt
