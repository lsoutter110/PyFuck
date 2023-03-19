# PyFuck
Esoteric transpiler to 12-character Python: `evalstr[]()+`

## Command line
`pyfuck.py` is invoked with the following arguments:
```
$ python pyfuck.py [SOURCE] [DESTINATION]
```
It is reccomended that `[SOURCE]` and `[DESTINATION]` are of type `.py` so they can be interpreted.

## Import
`pyfuck.py` can be imported:
```
from pyfuck import *
```
Importing `pyfuck` into a source file or the REPL will give access to:
```
from_ascii(str) -> str  | Converts the input character into a PyFuck string that evaluates to the character
from_str(str) -> str    | Converts the input string into a PyFuck string that evaluates to the string
number(int) -> str      | Converts the input number (>=0) into a PyFuck string that evaluates to the number
ind(int) -> str         | Converts the given input number (>=0) into a PyFuck index string that evaluates to the index
c: dict                 | A dictionary storing all of the base values used to calculate non-trivial cases, and some of those cases
```
**WARNING**: It is reccomended to _only_ use `from_str()`, as other functions do not return the best/any solution for some inputs.

TODO:
- Wrap it in a class
- Make a few more functions so it's more user friendly (`file_to_file()`, etc)
- Fix the "\n" bug - not sure how to fix the escape code problem right now
