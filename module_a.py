from .module_b import my_func_1
from .module_b import my_func_2

import os

# here on codeintel is broken, try to do "os." you will not manage to
# autocomplete, if you remove the dots in the imports it will work well