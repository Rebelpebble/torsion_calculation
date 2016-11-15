length = raw_input("Length (in): ")
width = raw_input("Width (in): ")
material_thickness = raw_input("Material Thickness (in): ")
force = raw_input("Force (lbs): ")
moment_arm = raw_input("Moment Arm (in): ")
shear_ultimate_strength = raw_input("Ultimate Shear Stress (psi): ")

mean_area = (length - material_thickness) * (width - material_thickness)

torque = force * moment_arm # in*lbs

shear_stress = torque / (2 * material_thickness * mean_area)

# Take 50% of the ultimate shear strength for a conservative estimate of
# the yeild strength of the material.
shear_yeild_strength = shear_ultimate_strength / 2.0

reserve_factor = shear_yeild_strength / shear_stress

print "Mean Area = %f in^2" % mean_area
print "Torque = %f in*lbs" % torque
print "Shear Stress = %f psi" % shear_stress
print "Reserve Factor = %f" % reserve_factor
