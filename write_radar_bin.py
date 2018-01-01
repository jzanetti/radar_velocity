import numpy
from scipy.io import FortranFile

"""
---------------------------------------
data structure
---------------------------------------
1. Data location information (dimension: 1):
    1.1 radar station:
        SSTN: radar station ID
        CLAT: radar station latitude
        CLON: radar station longitude
        HSMSL: height of station ground above msl
        
    1.2 beam (antenna)
        HSALG: height of antenna above ground
        ANEL: antenna elevation angle
        ANAZ: antenna azimuth angle
        QCRW: quality flag for the radial winds on this beam
        YEAR: year of observation this beam
        MNTH: month of observation this beam
        DAYS: day of observation this beam
        HOUR: hour of observation this beam
        MINU: minute of observation this beam
        SECO: second of observation this beam
    
    1.3 other info (not read in by GS):
        SCID: Radar scan ID (range 1-21)
        HNQV: high Nyquist velocity
        VOCP: volume coverage pattern
        VOID: radar volume ID (in the form of DDHHMM)
    
2. Radar data information (dimension: beam):
    DIST125M: distance from antenna to gate centre in units of 125m
    DMVR: Doppler mean radial velocity
    DVSW: Doppler velocity spectral width

"""

'''
-----------------------------
general
-----------------------------
'''
ntb = 1 # current beam number/ID

'''
-----------------------------
Data location information (dimension: 1)
-----------------------------
'''
SSTN = 13242    # radar station ID
CLAT = -40.0    # radar station latitude
CLON = 176.0    # radar station longitude
HSMSL = 120.0   # height of station ground above msl
HSALG = 127.0   # height of antenna above ground
ANEL = 0.7      # antenna elevation angle
ANAZ = 127.0    # antenna azimuth angle
QCRW = 1.0      # quality flag for the radial winds on this beam

hdr = [SSTN, CLAT, CLON, HSMSL, HSALG, ANEL, ANAZ, QCRW]

YEAR = 2017 # year of observation this beam
MNTH = 11 # month of observation this beam
DAYS = 15 # day of observation this beam
HOUR = 2 # hour of observation this beam
MINU = 0 # minute of observation this beam
SECO = 0 # second of observation this beam

hdr2 = [YEAR, MNTH, DAYS, HOUR, MINU, SECO]

SCID = 999
HNQV = 999
VOCP = 999
VOID = 999

hdr3 = [SCID, HNQV, VOCP, VOID]

''' 
-----------------------------
Radar data information (dimension: beam)
-----------------------------
'''
# number of gates for this beam
iret = 10
DIST125M = range(1, iret+1)

obs = numpy.ones((3, iret)) * -999.0
obs[0,:] = DIST125M
obs[1,2:5] = 6.0


''' 
-----------------------------
write data
-----------------------------
'''
numrwbin = 0
for i in range(0,iret):
    if obs[2,i] < 10000.0:
        numrwbin = numrwbin + 1

f = FortranFile('l2rwbufr.bin', 'w')
f.write_record(numpy.int64(ntb))
f.write_record(numpy.int64(numrwbin))
f.write_record(numpy.array(hdr,dtype=numpy.float64))
f.write_record(numpy.array(hdr2,dtype=numpy.float64))
f.write_record(numpy.array(hdr3,dtype=numpy.float64))

for i in range(0, iret):
    if obs[2,i] < 10000.0:
        f.write_record(numpy.array(obs[:,i],dtype=numpy.float64))

f.close()





