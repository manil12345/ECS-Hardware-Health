import requests
import json

# Set the ECS Management API endpoint and credentials
ecs_endpoint = "https://ecs.example.com:4443"
ecs_username = "username"
ecs_password = "password"

# Set the hardware status API endpoint
hardware_status_endpoint = f"{ecs_endpoint}/system/health/hardware-status"

# Set the headers for the hardware status request
hardware_status_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Send a GET request to retrieve the hardware status with the credentials and headers
hardware_status_response = requests.get(hardware_status_endpoint, auth=(ecs_username, ecs_password), headers=hardware_status_headers)

# Check if the request was successful
if hardware_status_response.status_code == 200:
    # Get the hardware status from the response JSON
    hardware_status = hardware_status_response.json()

    # Check the node status
    for node in hardware_status["nodes"]:
        node_name = node["name"]
        node_status = node["status"]
        print(f"Node '{node_name}' status: {node_status}")

    # Check the hard drive status
    for drive in hardware_status["drives"]:
        drive_name = drive["name"]
        drive_status = drive["status"]
        print(f"Drive '{drive_name}' status: {drive_status}")

    # Check the PSU status
    for psu in hardware_status["powerSupplies"]:
        psu_name = psu["name"]
        psu_status = psu["status"]
        print(f"PSU '{psu_name}' status: {psu_status}")

    # Check the fan status
    for fan in hardware_status["fans"]:
        fan_name = fan["name"]
        fan_status = fan["status"]
        print(f"Fan '{fan_name}' status: {fan_status}")
else:
    # Print an error message if the hardware status request was not successful
    print("Failed to retrieve hardware status.")
