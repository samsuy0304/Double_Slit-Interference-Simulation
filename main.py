#! /usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from Random import Random
import sys

if __name__ == "__main__":
    
    # Define constants
    wavelength = 1.0  # wavelength of the wave
    k = 2 * np.pi / wavelength  # wave vector
    slit_width = 0.1  # width of each slit
    slit_separation = 0.5  # separation between the slits
    screen_distance = 1.0  # distance from the slits to the screen
    screen_width = 1  # width of the screen
    screen_resolution = 1000  # number of screen pixels
    p_noise = 1
    random_noise = 0.1
    seed = 5555

    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: Muon.py s-seed [seed] -wave [wavelenght] -noise [random noise] -phase [phase_noise] -sw [slit_width] -ss [slit seperation] -scd [screen distance] -scw [screen width] -scr [screen resolution]" % sys.argv[0])
        sys.exit(1)

    if '-seed' in sys.argv:
        index = sys.argv.index('-seed')
        seed = int(sys.argv[index + 1])

    if '-wave' in sys.argv:
        index = sys.argv.index('-wave')
        wavelength = float(sys.argv[index + 1])

    if '-noise' in sys.argv:
        index = sys.argv.index('-noise')
        random_noise = float(sys.argv[index + 1])

    if '-phase' in sys.argv:
        index = sys.argv.index('-phase')
        p_noise = float(sys.argv[index + 1])

    if '-sw' in sys.argv:
        index = sys.argv.index('-sw')
        slit_width = float(sys.argv[index + 1])

    if '-ss' in sys.argv:
        index = sys.argv.index('-ss')
        slit_separation = float(sys.argv[index + 1])

    if '-scd' in sys.argv:
        index = sys.argv.index('-scd')
        screen_distance = float(sys.argv[index + 1])

    if '-scr' in sys.argv:
        index = sys.argv.index('-scr')
        screen_resolution = float(sys.argv[index + 1])

    if '-scw' in sys.argv:
        index = sys.argv.index('-scw')
        screen_width = float(sys.argv[index + 1])

    print("Configuring values...")
    
    Rand = Random(seed)

    # Create a file name using the constants
    file_name = f"output_wavelength{wavelength}_slitwidth{slit_width}_slitseparation{slit_separation}_screenwidth{screen_width}.png"
    file_name = file_name.replace('.', 'p')  # Replace '.' with 'p' in the file name


    print('Defining waves...')
    # Define the wave function
    def wave_function(x, y):
        # Define the amplitude of the wave
        A = 1.0
        # Calculate the distance from each slit to each point on the screen
        r1 = np.sqrt((x - slit_separation/2)**2 + y**2 + screen_distance**2)
        r2 = np.sqrt((x + slit_separation/2)**2 + y**2 + screen_distance**2)
        # Calculate the phase difference between the waves from each slit with random phase noise
        print("Adding phase Noise...")
        phase_noise = Rand.Random_Range(0, p_noise, size=x.shape)
        print("Adding random Noise...")
        phi = k * (r2 - r1) + phase_noise
        # Calculate the total wave amplitude at each point on the screen with random noise
        wave = A * np.cos(phi) + Rand.Normal(0, random_noise, size=x.shape)
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
    plt.savefig(file_name)
    plt.show()