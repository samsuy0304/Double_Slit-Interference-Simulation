import numpy as np
import matplotlib.pyplot as plt

class Pattern():
    def __init__(self, A=1.0, wavelenght=1.0, slit_width=0.1, slit_separation=0.5, screen_distance=1.0,
                 screen_width=1, screen_resolution=1000, p_noise=1, random_noise=0.1, seed=5555) -> None:
        self.A = A  # Amplitude of incoming wave
        self.wavelength = wavelenght  # wavelength of the wave
        self.k = 2 * np.pi / self.wavelength  # wave vector
        self.slit_width = slit_width  # width of each slit
        self.slit_separation = slit_separation  # separation between the slits
        self.screen_distance = screen_distance  # distance from the slits to the screen
        self.screen_width = screen_width  # width of the screen
        self.screen_resolution = screen_resolution  # number of screen pixels
        self.p_noise = p_noise
        self.random_noise = random_noise
        self.seed = seed

    def GenerateWave(self):
        # Calculate the interference pattern on the screen using vectorized operations
        x = np.linspace(-self.screen_width / 2, self.screen_width / 2, self.screen_resolution)
        y = np.linspace(0, self.screen_distance, self.screen_resolution)
        X, Y = np.meshgrid(x, y)

        # Optimize the interference pattern calculation
        R1 = np.sqrt((X - self.slit_separation / 2) ** 2 + Y ** 2 + self.screen_distance ** 2)
        R2 = np.sqrt((X + self.slit_separation / 2) ** 2 + Y ** 2 + self.screen_distance ** 2)
        PHI = self.k * (R2 - R1) + np.random.random(size=X.shape)
        WAVE = self.A * np.cos(PHI) + np.random.normal(0, self.random_noise, size=X.shape)
        Z = WAVE ** 2
        
        return Z

# Create an instance of the Pattern class
pattern_instance = Pattern(A=2,screen_resolution=6)

# Call the GenerateWave method on the instance
pattern_instance.GenerateWave()
