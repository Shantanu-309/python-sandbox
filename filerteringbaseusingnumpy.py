import numpy as np
ages =  np.array([35,6,78,34,22,42,21,57,23,43,32,23,14,16,76,19,46,37,34,86])

teenagers = ages[(ages<18) & (ages>12)]
adults = ages[(ages>=18)&(ages<60)]
seniors = ages[ages>=60]
