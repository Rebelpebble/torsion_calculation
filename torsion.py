# Take 50% of the ultimate shear strength for a conservative estimate of
# the yeild strength of the material.
YIELD_REDUCTION_FACTOR = 0.5

length = float(raw_input("Length (in): "))
width = float(raw_input("Width (in): "))
material_thickness = float(raw_input("Material Thickness (in): "))
force = float(raw_input("Force (lbs): "))
moment_arm = float(raw_input("Moment Arm (in): "))
shear_ultimate_strength = float(raw_input("Ultimate Shear Stress (psi): "))

mean_area = (length - material_thickness) * (width - material_thickness)

torque = force * moment_arm

shear_stress = torque / (2 * material_thickness * mean_area)

shear_yield_strength = shear_ultimate_strength * YIELD_REDUCTION_FACTOR

reserve_factor = shear_yield_strength / shear_stress

print "Mean Area = %.2f in^2" % mean_area
print "Torque = %.2f in*lbs" % torque
print "Shear Stress = %.0f psi" % shear_stress
print "Reserve Factor = %.2f" % reserve_factor
