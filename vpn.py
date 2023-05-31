import subprocess
import sys
import yaml

def connect_vpn(config_file):
    # Read YAML configuration file
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    vpn_name = list(config.keys())[0]
    vpn_data = config[vpn_name]

    path = vpn_data.get('path to file')
    username = vpn_data.get('username')
    password = vpn_data.get('password')

    # Check if the required fields are present
    if not all((path, username, password)):
        print("Invalid or incomplete configuration file.")
        return

    # Start OpenVPN connection
    command = [
        'sudo', 'openvpn',
        '--config', path,
        '--auth-user-pass', '/dev/stdin',
        '--daemon'
    ]
    subprocess.run(command, input=f"{username}\n{password}\n", text=True)
    print("OpenVPN connection has been started in the background.")

def disconnect_vpn():
    # Kill the OpenVPN connection
    subprocess.run("sudo pkill openvpn", shell=True)
    print("OpenVPN connection has been terminated.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python vpn_connect.py <config_file> [connect|disconnect]")
        sys.exit(1)

    config_file = sys.argv[1]
    action = sys.argv[2]

    if action == 'connect':
        connect_vpn(config_file)
    elif action == 'disconnect':
        disconnect_vpn()
    else:
        print("Invalid action. Please choose either 'connect' or 'disconnect'.")
