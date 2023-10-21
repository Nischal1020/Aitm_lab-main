import subprocess
from file_name import RandomNumberGenerator

# Create an instance of RandomNumberGenerator
rng = RandomNumberGenerator("picture_name.xlsx")
rng.generate_and_print_random_numbers()

# Get the generated name
name = rng.name[-1]  # Assuming you want the last generated name

# Define the command to run
command = f"fswebcam {name}.jpg"

# Run the command using subprocess
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
else:
    print("Command executed successfully")
