import time, math
m = float(input("Mass: \n"));
sf = 1.05*float(input("Surface area: \n"));
#assuming cubic satellite
alt = int(input("Altitude of circular orbit (km): \n"));
flux = int(input("Expected solar flux at 10.7cm (recommend 65): \n"));
Ap = int(input("Expected geomagnetic A index (recommend 5): \n"));
Re = 6378000;
Me = 5.98E24;
G = 6.67E-11;
t = 0;
dt = 0.1;
dtd = dt*3600*24;
dalt = 10;
alt2 = alt;
R = Re + alt*1000;
P = (2*math.pi)*(math.sqrt((R**3)/Me/G));

print("DECAY MODEL GENERATED AT ", time.strftime('%l:%M%p %Z on %b %d, %Y'));
print("TIME       HEIGHT       PERIOD       MEAN MOTION       DECAY");
print("(days)      (km)        (mins)        (rev/day)      (rev/day^2)");

while alt>180:
    sh = (900 + 2.5*(flux - 70) + 1.5*Ap)/(27 - 0.012*(alt - 200));
    rho = 6E-10*math.exp(-1*(alt - 175)/sh);
    dP = 3*math.pi*(sf/m)*R*rho*dtd;
    if alt <= alt2:
        Pp = P / 60;                    #converted to minutes
        MM = 1440 / Pp;                 #meanmotion
        nMM = 1440/(P - dP)/60;         #newMM
        Decay = dP/dt/P*MM;
        print(round(t, 1), "    ", round(alt, 1), "       ", round(Pp, 1), "         ", round(MM, 1), "         ", round(Decay, 1));
        alt2 -= dalt;
    P = P - dP;
    t = t + dt;
    R = (G*Me*P*P/4/math.pi/math.pi)**(1./3);
    alt = (R - Re)/1000;
print("Solar output assumed consistent.");
print("Re-entry expected after ", round(t, 1), " days (", round(t/365, 1), " years)");