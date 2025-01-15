import numpy as np

"""""
Given the complex numbers z1 = −2 + j and z2 =sqrt(5) e^(j3π/4)
4 , calculate values that result
from the following operations showing all steps clearly by hand (using a calculator when
needed) and give each answer in the form noted.
(a) z1 + z2 in rectangular form
(b) z1z2 in polar form using phasor notation (angle in degrees)
(c) z1/z2 in polar form using a complex exponential (angle in radians)
"""""
z1real = -2
z1imag = 1

z2angleRadians = (3 * np.pi) / 4
z2radius = np.sqrt(5)

# a) z1 +z2 in rec form

z2real = z2radius * np.cos(z2angleRadians)  # Calculating z2Real
z2imag = z2radius * np.sin(z2angleRadians)  # Calculating z2Imag
# print(z2real, z2imag)
realSum = z2real + z1real
imagSum = z2imag + z1imag

print(f"z1 + z2= ({round(realSum, 2)} + j {round(imagSum, 2)})")

# b) z1*z2

z1radius = np.sqrt(z1real ** 2 + z1imag ** 2)  # Using Pythagorean therm to solve for radius
print(f"z1radius = {z1radius}")

z1angleRadians = np.arctan2(z1imag, z1real)  # Calculating z1 angle
print(f"z1angleRadians = {z1angleRadians}")

z1angleDegrees = np.degrees(round(z1angleRadians,2))   # Converting z1 from radians to degrees
print(f"z1angleDegrees = {round(z1angleDegrees, 2)}")

z2angleDegrees = np.degrees(round(z2angleRadians,2))
print(f"z1+z2  cos degrees= {np.cos(z1angleDegrees+z2angleDegrees)}")

z1z2ProductReal = (z1radius*z2radius)*(np.cos((np.radians(z1angleDegrees+z2angleDegrees))))
z1z2Productimag = (z1radius*z2radius)*(np.sin(np.radians(z1angleDegrees+z2angleDegrees)))

print(f"z1*z2= ({round(z1z2ProductReal, 2)} + j {round(z1z2Productimag , 2)})")


# (c) z1/z2 in polar form using a complex exponential (angle in radians)
z1z2quotientReal= (z1radius/z2radius)*np.cos(round(z1angleRadians-z2angleRadians,2))
z1z2quotientImag= (z1radius/z2radius)*np.sin(round(z1angleRadians-z2angleRadians,2))
print(f"z1/z2= ({round(z1z2quotientReal, 2)} + j {round(z1z2quotientImag, 2)})")




