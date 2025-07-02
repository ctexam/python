from pylab import *
m = 1.0 
k = 1.0 # Force constant 
c = 0.4# Damping coeƯ icient
gamma = c/m 
omega2 = k/m 
lx = [] 
ly = [] 
def f(t, S): 
    x, v = S # dx/dt and dv/dt 
    return array([v, -gamma*v-omega2*x]) 
def shmrk4(ti, Si, tf, h=0.01): 
    while ti <= tf: 
        lx.append(Si[0]) 
        ly.append(Si[1]) 
        k1 = h * f(ti, Si) 
        k2 = h * f(ti + 0.5*h, Si + 0.5*k1) 
        k3 = h * f(ti + 0.5*h, Si + 0.5*k2) 
        k4 = h * f(ti + h, Si + k3) 
        Si += (k1 + 2*k2 + 2*k3 + k4)/6 
        ti += h 
x0 = 1.0 # Initial x and v 
v0 = 0.0 
Si = array([x0, v0]) 
shmrk4(0, Si, 20) 
plot(lx, ly) 
xlabel("Displacement (x)") 
ylabel("Velocity (v)") 
title("Phase-Space Diagram of Damped Harmonic Oscillator") 
grid(True) 
show() 