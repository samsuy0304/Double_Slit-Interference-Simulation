import numpy as np
import matplotlib.pyplot as plt

# Define constants
wavelength = 1.0  # wavelength of the wave
k = 2 * np.pi / wavelength  # wave vector
slit_width = 0.1  # width of each slit
slit_separation = 0.5  # separation between the slits
screen_distance = 1.0  # distance from the slits to the screen
screen_width = 2.0  # width of the screen
screen_resolution = 1000  # number of screen pixels

# Define the wave function
def wave_function(x, y):
    # Define the amplitude of the wave
    A = 1.0
    # Calculate the distance from each slit to each point on the screen
    r1 = np.sqrt((x - slit_separation/2)**2 + y**2 + screen_distance**2)
    r2 = np.sqrt((x + slit_separation/2)**2 + y**2 + screen_distance**2)
    # Calculate the phase difference between the waves from each slit
    phi = k * (r2 - r1)
    # Calculate the total wave amplitude at each point on the screen
    wave = A * np.cos(phi)
    return wave

# Calculate the interference pattern on the screen
x = np.linspace(-screen_width/2, screen_width/2, screen_resolution)
y = np.linspace(0, screen_distance, screen_resolution)
X, Y = np.meshgrid(x, y)
Z = wave_function(X, Y)**2

# Plot the interference pattern
plt.imshow(Z, cmap='gray', extent=[-screen_width/2, screen_width/2, 0, screen_distance])
plt.xlabel('Position on screen (m)')
plt.ylabel('Distance from slits (m)')
plt.savefig("Wave_"+str(wavelength) +"m_Slit_"+str(slit_width)+".png")
plt.show()
