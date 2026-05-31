import sys

import fontforge

f = fontforge.open(sys.argv[1])
print(dir(f))
