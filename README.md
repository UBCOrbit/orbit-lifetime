# orbit-lifetime
Python - calculates the lifetime of a satellite in a circular orbit given its specifications.\n
Requires input of satellite mass, surface area and altitude in km. The csv file is required to provide Ap indices. Cubesat standards are 1.33 kg and 0.01 square metres.\n
Model assumes satellite is presenting a face forward. If angled, change 1.05 to 0.8 in the first few lines of the code.
Model is set to launch date of June 2021.\n
Atmosphere uses a simple model that takes solar 10.7cm radio flux and geomagnetic index Ap to find scale height and density at required altitude.\n
Radio flux data are predictions by NASA for solar Cycle 25 beginning April 2020, with a standard undertainty of six months. This data was divided into growth and decay and each fitted to a gaussian function using 3 parameters and a chi-square minimisation. Cycles are assumed to be 11.3 years and identical to the prediction for 25. Spreadsheet contains prediction and model comparisons. Note: The recent Cycle 24 was double-peaked, if this is the case for future cycles lifetime may be shortened.\n
Geomagnetic Ap index uses the history of Cycle 24, applied to all future cycles. Model assumes no hits from high-energy coronal mass ejections; an M or X class flare could cause a loss of up to 10-30 kilometres over several days\n
