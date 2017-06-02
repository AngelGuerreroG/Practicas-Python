#VISUAL DEFINE

from visual import * #allows the program to run and create visual actions 
from visual.graph import * #allows the program to create graphs based on the code
from random import random

scene = display (title = 'Sistema solar', width = 800, height = 800, \
                 range = (25000,25000,25000), center = (0,0,0)) #sets up the window to view the program 
scene.autoscale = True #commands the scene to scale on its own when necessary


labels = ["sun", "mercury", "venus", "earth", "moon","mars", "jupiter",\
         "saturn", "uranus","neptune", "pluto"]

radii = {"sun": 150, "mercury": 45, "venus": 50, "earth": 50, "moon": 10, \
         "mars": 45, "jupiter": 90, "saturn": 75 , "uranus": 80, \
         "neptune": 73, "pluto": 35}

position = {"sun": (0, 0, 0), "mercury": (210.0,0,0), "venus": (383.664,0,0),"earth": (516.664,0,0), \
            "moon": (516.664+5.0,0,0),"mars": (787.222,0,0), "jupiter": (2688.068,0,0),\
            "saturn": (4920.048,0,0), "uranus": (9924.19,0,0),"neptune": (16544.811,0,0), "pluto": (28534.968,0,0)}

# scaling factors
sr = 1 # radius scale


obj = dict()
mat = {"sun": materials.emissive, "mercury": materials.wood, "venus": materials.wood, \
       "earth": materials.BlueMarble, "moon": materials.emissive,"mars": materials.wood, \
       "jupiter": materials.marble,"saturn": materials.marble, \
       "uranus": materials.wood,"neptune": materials.wood, "pluto":materials.wood}

col = {"sun": color.yellow, "mercury": color.cyan, "venus": color.orange, "earth": color.blue, "moon": color.white, \
       "mars": color.red, "jupiter": color.cyan,"saturn": color.blue, \
       "uranus": color.magenta,"neptune": color.red, "pluto": color.white}

vel = {"mercury": vector(0,0,295), "venus": vector(0,0,225), "earth": vector(0,0,195), "moon": vector(0,0,195),\
       "mars": vector(0,0,155), "jupiter": vector(0,0,70),"saturn": vector(0,0,50), "uranus": vector(0,0,30),\
       "neptune": vector(0,0,23), "pluto": vector(0,0,15)}

rotation = { "sun": 0, "mercury": 10, "venus": 20, "earth": 30, "moon": 1,"mars": 15, "jupiter": 15,\
         "saturn": 15, "uranus": 15,"neptune": 15, "pluto": 15}

for l in labels:
    c = col[l]
    o = sphere(pos = position[l], radius = sr * radii[l], material = mat[l], color = c) #DEFINING PLANETS AS SPHERES
    o.trail = curve(color = c)
    if l in vel:
        o.velocity = vel[l]
    obj[l] = o


#Although these positions do not represent the exact distances of each of the planets from the sun, they are to scale in relation to each other 
#The ratio of the distances between each of the planets is to scale with our solar system 
#The ratio of the distance of mercury to the sun in comparison to the distances of all the other planets to the sun is the same as the true ratio in our solar system

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#DEFINING CONSTANTS FOR CALCULATIONS MADE WHILE PROGRAM IS RUNNING
scale = 20
    
G = -6.7 * 10**(-4) #  N*Km2/Ton2

# Masses in metric tons
#Since vpython cannot handle numbers as large as the true masses of the planets:
#1 divided all of the real planet masses by 1*10**20 (the scale defined above)
#Also that they are all scaled to each other even though they are smaller than the true values 
#For the purposes of calculations, the masses are still in kg, they are simply scaled to each other in smaller numbers

# masses in metric tons

mass = {"sun": 1.988*10**(30 - scale),"mercury": 3.29*10**(20 - scale), \
        "venus": 4.87*10**(21 - scale), "earth": 6*10**(21 - scale), \
        "moon": 7.35*10**(19 - scale), "mars": 6.39*10**(20 - scale), \
        "jupiter": 1.90*10**(24 - scale), "saturn": 5.68*10**(23 - scale), \
        "uranus": 8.610*10**(22 - scale), "neptune": 1.02*10**(23 - scale), \
        "pluto": 1.31*10**(19 - scale), "spaceship": 7*10**(25 - scale)  }


# The real ratios of planet speeds to Earth's during orbit
#the real ratio speeds during their orbits

ratio = {"sun": 0, "mercury": 1.600, "venus": 1.177 , "earth": 1.000, "moon": 1.000,"mars": 0.805, "jupiter": 0.437,\
         "saturn": 0.324, "uranus": 0.228,"neptune": 0.182, "pluto": 0.158}

t = 0 #initial time is 0 seconds
deltat = .02 #defines deltat change in time the calculations are made every .005 "seconds", as this is the defined change in time
#time_interval = 0.5 #creates the time interval for plotting on the graphs
#time_interval_int = int(time_interval/deltat) #adjusts the time interval based on the defined deltat

#---------------------------------------------------------------------------------------------------------------------
#CREATING THE "while" LOOP

t = 0
dt = 1000
c = 500
logfile = open("velocidades.txt", "w")
logfile2 = open ("posiciones.txt","w")
while c > 0: #program will run while t is less than 3000 seconds
    rate (10000) #controls the speed of the program so it only goes through the loop 1000 times per second

    #-----------------------------------------------------------------------------------------------------------------
    #CREATING THE MOTION LOOP

    if t % dt == 0:
        c -= 1
    for l in labels:

        if l == "sun":
            continue
        if t % dt == 0:
            print >>logfile, "%d, %s, %f" % (t, l, mag(o.velocity))
            print >>logfile2, "%d, %s, %s" % (t, l,(o.pos))
        o = obj[l]
        o.trail.append(pos = o.pos) 
        d = mag(o.pos)
        if d <= radii["sun"]: break
        uv = (o.pos - obj["sun"].pos) / d      
        m = mass[l]
        f = (G*mass["sun"] * m * uv) / d**2 
        o.velocity += (f / m) * deltat
        o.pos += o.velocity * deltat 
        o.rotate(angle = radians(rotation[l]), axis=(0,1,0)) 
        ratio[l] = mag(o.velocity) / mag(obj["earth"].velocity) 
       
    t += 1
            
logfile.close()


