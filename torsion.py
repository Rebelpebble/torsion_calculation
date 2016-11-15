import math

l = 0.356 #in
d = 0.205 #in

t = (l - d) / 2
print "t = %f in" % t #in

# Calculate Am
l_prime = l - t
Am = l_prime ** 2
print "Mean Area = %f in^2" % Am

# Calculate Torque
f = 5 #pounds
arm = 1.5 * 12 #inches
T = f * arm # in*lbs
print "Torque = %f in*lbs" % T

# Calculate Shear
c = math.sqrt(2 * ((l / 2) ** 2))
tau = T / (2 * c * Am)
print "tau = %f psi" % tau

tsu = 35000 #psi
Vu = tsu * 0.5
RF = Vu / tau
print "RF = %f" % RF

print "Done"
