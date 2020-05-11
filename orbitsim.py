#valid 180-500km!!!
import time, math, csv
m = float(input("Mass: \n"))
sf = 1.05*float(input("Surface area: \n"))
#assuming cubic satellite
alt = int(input("Altitude of circular orbit (km): \n"))
#flux = int(input("Expected solar flux at 10.7cm (recommend 100): \n"))
#Ap = int(input("Expected geomagnetic A index (recommend 5): \n"))

Re = 6378000
Me = 5.98E24
G = 6.67E-11
date = [2021, 6]
t = 0
dt = 0.1
dtd = dt*3600*24
dalt = 10
alt2 = alt
R = Re + alt*1000
P = (2*math.pi)*(math.sqrt((R**3)/Me/G))

print("DECAY MODEL GENERATED AT ", time.strftime('%l:%M%p %Z on %b %d, %Y'))
print("LAUNCH DATE: JUNE 2021")
print("TIME       HEIGHT       PERIOD       MEAN MOTION")
print("(days)      (km)        (mins)        (rev/day)")

def flux():
    time = t
    while time > 4123:
        time -= 4123
    if time <= 1462:
        #see heliology model
        return 78.904*math.exp((-(time-1462)**2)/(1130**2))+57.35
    elif time > 1462 and time <= 3775:
        return (65.994* math.exp(-((time - 1492)**2) / (1260**2)) + 69.449)
    elif time >3775 and time <= 4124:
        return 70;
    elif time > 4124:
        print("line 38 error:time exceeded", time)
        exit()
with open('ap24.csv', newline='') as csvfile:
    csvdata = list(csv.reader(csvfile))[0]
def Ap():
    time = t
    while time > 4124:
        time -= 4124
    if math.floor(time/(365/12)) > 124:
        return 5.8
    else:
        return float(csvdata[math.floor(time/(365/12))])

while alt>180:
    #pseudopressure scale height=RT/Mg = temperature/mean molecular mass of atmosphere
    sh = (900 + 2.5*(flux() - 70) + 1.5*Ap())/(27 - 0.012*(alt - 200))
    #atmospheric density at this height
    rho = 6E-10*math.exp(-1*(alt - 175)/sh)
    dP = 3*math.pi*(sf/m)*R*rho*dtd
    if alt <= alt2:
        Pp = P / 60                    #converted to minutes
        MM = 1440 / Pp                 #meanmotion
        nMM = 1440/(P - dP)/60         #newMM
        Decay = dP/dt/P*MM
        print(round(t, 1), "    ", round(alt, 1), "       ", round(Pp, 1), "         ", round(MM, 1))
        alt2 -= dalt
    P = P - dP
    t = t + dt
    R = (G*Me*P*P/4/math.pi/math.pi)**(1./3)
    alt = (R - Re)/1000

print("Assumptions: No damaging storms, radiation pressure and magnetic reaction forces negligible.")
print("Cycles 24 and 25 are of low amplitude; lifetime likely represents high estimate")
print("Future solar cycles assumed 11.3 yr in length and aligning with latest Cycle 25 predictions")
print("Geomagnetic data assumed repeat of Cycle 24")
print("Re-entry expected within ", round(t, 1), " days (", round(t/365, 1), " years)")

date[0]+=math.floor(t/365)
date[1]+=math.floor((t-math.floor(t/365)*365)/365*12)
if date[1]>12:
    date[0]+=1
    date[1]-=12;
months = ["Jan", "Feb" , "Mar" , "Apr" , "May", "Jun" , "Jul" , "Aug" , "Sep", "Oct" , "Nov", "Dec"]
print("Re-entry expected by ", months[date[1]], date[0])