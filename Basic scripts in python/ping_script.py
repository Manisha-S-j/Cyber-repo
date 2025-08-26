import os

# Step 1: Ask the user for a website
host = input("Enter website to ping: ")

# Step 2: Run the ping command (works only on Windows here)
# On Linux/Mac, replace -n with -c
response = os.system(f"ping -n 4 {host}")

# Step 3: Show result
if response == 0:
    print(f"{host} is reachable ")
else:
    print(f"{host} is not reachable ")
