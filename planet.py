import numpy as np
import matplotlib.pyplot as plt
import os

def create_image(time_setting, mode_text, output_folder):
    auunit = 1.495978707 * 100

    earth_au = 1 * auunit
    mars_au = 1.523679 * auunit
    jupiter_au = 5.204267 * auunit
    saturn_au = 9.53707032 * auunit
    uranus_au = 19.19126393 * auunit
    neptune_au = 30.06896348 * auunit

    earth_period = 365.2564
    mars_period = 686.971
    jupiter_period = 4332.59
    saturn_period = 10756.1995
    uranus_period = 30707.4896
    neptune_period = 60223.3528

    time = np.linspace(0, time_setting, 1000)

    earth_x = earth_au * np.cos(2 * np.pi * time / earth_period)
    earth_y = earth_au * np.sin(2 * np.pi * time / earth_period)

    mars_x = mars_au * np.cos(2 * np.pi * time / mars_period)
    mars_y = mars_au * np.sin(2 * np.pi * time / mars_period)

    jupiter_x = jupiter_au * np.cos(2 * np.pi * time / jupiter_period)
    jupiter_y = jupiter_au * np.sin(2 * np.pi * time / jupiter_period)

    saturn_x = saturn_au * np.cos(2 * np.pi * time / saturn_period)
    saturn_y = saturn_au * np.sin(2 * np.pi * time / saturn_period)

    uranus_x = uranus_au * np.cos(2 * np.pi * time / uranus_period)
    uranus_y = uranus_au * np.sin(2 * np.pi * time / uranus_period)

    neptune_x = neptune_au * np.cos(2 * np.pi * time / neptune_period)
    neptune_y = neptune_au * np.sin(2 * np.pi * time / neptune_period)

    plt.figure(figsize=(8, 6))

    plt.plot(mars_x - earth_x, mars_y - earth_y, label='Mars', color='salmon')
    plt.plot(jupiter_x - earth_x, jupiter_y - earth_y, label='Jupiter', color='goldenrod')
    plt.plot(saturn_x - earth_x, saturn_y - earth_y, label='Saturn', color='darkgoldenrod')
    plt.plot(uranus_x - earth_x, uranus_y - earth_y, label='Uranus', color='turquoise')
    plt.plot(neptune_x - earth_x, neptune_y - earth_y, label='Neptune', color='steelblue')

    plt.xlabel('X (10^6 km)')
    plt.ylabel('Y (10^6 km')

    plt.legend()
    plt.title(f"Exoplanets' Movement at {time_setting} {mode_text}")
    plt.grid(True)

    file_name = f"{output_folder}/exoplanets_movement_{time_setting}_{mode_text}.png"
    plt.savefig(file_name)
    plt.close()

def main():
    start_time = int(input("Initial time: "))
    time_step = int(input("Time interval: "))
    total_images = int(input("Total images: "))
    mode_text = input("Enter 'days' or 'years' mode: ")

    output_folder = "exoplanet_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(total_images):
        time_setting = start_time + i * time_step
        create_image(time_setting, mode_text, output_folder)

if __name__ == "__main__":
    main()
