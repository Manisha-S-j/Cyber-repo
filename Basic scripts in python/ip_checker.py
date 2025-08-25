import socket
domain = input("Enter your domain(i.e, google.com or any of your choice) : ")
try:

    ip_address = socket.gethostbyname(domain)
    print(f"The IP address of {domain} is: {ip_address}")
except:
    print("Invalid domain name. Please try again.")