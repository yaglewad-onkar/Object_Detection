import requests
import sys
import json

def control_led(ip_address, action, brightness=None, color=None):
    base_url = f"http://{ip_address}/json/state"

    if action == "on":
        payload = {"on": True}
    elif action == "off":
        payload = {"on": False}
    elif action == "brightness" and brightness is not None:
        payload = {"bri": brightness}
    elif action == "color" and color is not None:
        # Assuming color is a list of RGB values, e.g., [255, 0, 0]
        payload = {"seg": [{"col": [color]}]}
    else:
        print("Invalid action. Use 'on', 'off', 'brightness', or 'color'.")
        return

    # Send the POST request with JSON payload
    response = requests.post(base_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

    # Print the response
    print(response.text)

if __name__ == "__main__":
    # Replace "YOUR_IP_ADDRESS" with your actual IP address
    ip_address = "192.168.43.150"

    if len(sys.argv) < 2:
        print("Usage: python control_led.py <action> [brightness] [color]")
        sys.exit(1)

    action = sys.argv[1].lower()

    if action == "brightness" and len(sys.argv) == 3:
        brightness = int(sys.argv[2])
        control_led(ip_address, action, brightness)
    elif action == "color" and len(sys.argv) == 5:
        # Assuming color is provided as three separate values: R, G, B
        color = [int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]
        control_led(ip_address, action, color=color)
    else:
        control_led(ip_address, action)
