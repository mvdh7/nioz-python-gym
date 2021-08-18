import numpy as np

_rng = np.random.default_rng(1)
npts = 10
temperature = _rng.normal(loc=20, scale=6, size=npts)
temperature[5] = 18
temperature[8] = 21
salinity = _rng.normal(loc=35, scale=3, size=npts)
salinity[3] = 35
_testarr = _rng.normal(loc=15, scale=15, size=(20, 30, 40))

_testarr[0, 0, 0] = 18
_testarr[0, 0, 1] = 21
_testarr[0, 0, 2] = 35
_testarr[0, 0, 3] = 0


x = 2
y = 2
