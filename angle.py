#given a rt angle triangle and a perpendicular is kept from a corner to the hypotenus
# | \
# |  \
# |   \
# |____\

import math
ab=int(input())
bc=int(input())

p=math.atan(ab/bc)
print(str(round(math.degrees(p)))+"°")
