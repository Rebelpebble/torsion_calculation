# Take 50% of the ultimate shear strength for a conservative estimate of
# the yeild strength of the material.
YIELD_REDUCTION_FACTOR = 0.5

length = raw_input("Length (in): ")
width = raw_input("Width (in): ")
material_thickness = raw_input("Material Thickness (in): ")
force = raw_input("Force (lbs): ")
moment_arm = raw_input("Moment Arm (in): ")
shear_ultimate_strength = raw_input("Ultimate Shear Stress (psi): ")

mean_area = (length - material_thickness) * (width - material_thickness)

torque = force * moment_arm

shear_stress = torque / (2 * material_thickness * mean_area)

shear_yield_strength = shear_ultimate_strength * YIELD_REDUCTION_FACTOR

reserve_factor = shear_yield_strength / shear_stress

print "Mean Area = %f in^2" % mean_area
print "Torque = %f in*lbs" % torque
print "Shear Stress = %f psi" % shear_stress
print "Reserve Factor = %f" % reserve_factor
