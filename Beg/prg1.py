# You are a pilot, cruising at an altitude of 33000 ft,

# you want to land your plane, to land your plane, you need

# to be under 5000ft take input from the pilot, what

# is your current altitude, and suggest

# the pilot to go around if the altitude is more than 10K feet,

# if its more than 5K suggest the pilot to land the plane

# by bringing it to 1000ft

GO = "GO!!!!  CAP, letss gooooo!!!"
GO_DOWN = "its tooo high Cap, lets land sir"
GO_LAND = "YO! Cap its time lets get down!!!"
altitude = 33000
max_altitude = int(10000)
min_altitude = int(5000)
new_altitude = int(input("Whats the altitude now cap ?? "))
int(new_altitude)
print(type(new_altitude))
if new_altitude > min_altitude:
    print(f"{GO_LAND}")
elif new_altitude > max_altitude:
    print(f"{GO_DOWN}")
else:
    print(f"{GO}")
