
# VPN Connect Script :rocket:

This script allows you to easily connect to and disconnect from an OpenVPN server using a YAML configuration file.

## Prerequisites

- Python 3.x installed
- `pyyaml` module installed (`pip install pyyaml`)
- `sudo` access to run the script with administrative privileges

## Installation

1. Clone the repository or download the `vpn_connect.py` script to your local machine.

2. Install the required Python module:

   ```shell
   pip install pyyaml
   ```

## Usage

1. Create a YAML configuration file with the VPN details.

   Example YAML file (`vpn_config.yml`):

   ```yaml
   USA:
     path to file: /home/user/vpns/usa.ovpn
     username: 118fcg0b10999b742796q7fd0551b77d
     password: 0000000021dbc5ce8b4555d92d6wsc5f7a38079836e7e986
   ```

   Make sure to replace the placeholders with the actual values of your VPN configuration.

2. To connect to the VPN:

   ```shell
   python vpn.py vpn_config.yml connect
   ```

   The script will read the configuration file and establish the VPN connection in the background.

3. To disconnect from the VPN:

   ```shell
   python vpn_connect.py disconnect
   ```

   The script will terminate the OpenVPN connection.

## Troubleshooting

- If you encounter any errors while running the script, please ensure that you have the necessary permissions to run the script with `sudo`.

- Double-check your YAML configuration file for any formatting issues. Ensure that the indentation is done using tabs (not spaces) consistently.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
