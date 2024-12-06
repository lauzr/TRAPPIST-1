from skyfield import api
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
import numpy as np
import pandas as pd

# Loading the ephemeris and defining the planets
planets = load('de421.bsp')
sun, earth, moon, mercury, mars, venus, jupiter, saturn, uranus, neptune, pluto = planets['sun'], planets['earth'], planets['moon'], planets['mercury'],planets['mars'], planets['venus'], planets['jupiter barycenter'], planets['saturn barycenter'], planets['uranus barycenter'], planets['neptune barycenter'], planets['pluto barycenter'] 
# The Timescale object returned by load.timescale() manages the conversions between different time scales 
ts = load.timescale()

# ------------------------------------------
# Building an array of moments in time, by number of days as observations
days = []

def createList(r1, r2):
    return list(range(r1, r2+1))

# Using the range of 0 to 394 to cover fom September 2024 to September 2025
r1, r2 = 0, 394
days = createList(r1, r2)

# Time of observation; given a specific date and how many following days
t0 = ts.utc(2024, 9, 1, days)
# --------------------------------------------
# Empty arrays for the planets 
earth_values = []
moon_values = []
mercury_values = []
venus_values = []
mars_values = []
jupiter_values = []
saturn_values =[]
uranus_values = []
neptune_values = []
pluto_values =[]

# Getting the position of each planet in relation to the sun
# Galactic coordinates are measured against the disc of our own Milky Way galaxy, as measured from our vantage point here inside the Orion Arm
# Skyfield uses the IAU 1958 Galactic System II for the estimates of the galaxies orientation, which is believed to be accurate to within ±0.1°.
# This returns the cordinates of positon on that frame
# Longitude 0°–360° east from galactic center
# Adding that degree to the corresponding array
earthpos = planets['sun'].at(t0).observe(planets['earth'])
late, lone, distancee = earthpos.frame_latlon(ecliptic_frame)
earth_values = lone.degrees

moonpos = planets['sun'].at(t0).observe(planets['moon'])
latm, lonm, distancem = moonpos.frame_latlon(ecliptic_frame)
moon_values = lonm.degrees

mercurypos = planets['sun'].at(t0).observe(planets['mercury'])
latme, lonme, distanceme = mercurypos.frame_latlon(ecliptic_frame)
mercury_values = lonme.degrees

venuspos = planets['sun'].at(t0).observe(planets['venus'])
latv, lonv, distancev = venuspos.frame_latlon(ecliptic_frame)
venus_values = lonv.degrees

marspos = planets['sun'].at(t0).observe(planets['mars'])
latma, lonma, distancema = marspos.frame_latlon(ecliptic_frame)
mars_values = lonma.degrees

jupiterpos = planets['sun'].at(t0).observe(planets['jupiter barycenter'])
latj, lonj, distancej = jupiterpos.frame_latlon(ecliptic_frame)
jupiter_values = lonj.degrees

saturnpos = planets['sun'].at(t0).observe(planets['saturn barycenter'])
lats, lons, distances = saturnpos.frame_latlon(ecliptic_frame)
saturn_values = lons.degrees

uranuspos = planets['sun'].at(t0).observe(planets['uranus barycenter'])
latu, lonu, distanceu = uranuspos.frame_latlon(ecliptic_frame)
uranus_values = lonu.degrees

neptunepos = planets['sun'].at(t0).observe(planets['neptune barycenter'])
latn, lonn, distancen = neptunepos.frame_latlon(ecliptic_frame)
neptune_values = lonn.degrees

plutopos = planets['sun'].at(t0).observe(planets['pluto barycenter'])
latp, lonp, distancep = plutopos.frame_latlon(ecliptic_frame)
pluto_values = lonp.degrees

# Creating a dataframe by combining all the planets with the arrays of values 395 rows, for unique instances (days), across 10 columns
df=pd.DataFrame(earth_values, columns=['earth'])
df['moon'] = moon_values 
df['mercury'] = mercury_values 
df['venus'] = venus_values 
df['mars'] = mars_values 
df['jupiter'] = jupiter_values 
df['saturn'] = saturn_values 
df['uranus'] = uranus_values 
df['neptune'] = neptune_values 
df['pluto'] = pluto_values
print(df)

df.to_excel('helio_degrees.xlsx')
# print(t0)



