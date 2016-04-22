Automation Scripts
===

local-dev.py
---
A simple Python script to setup a local development environment in seconds via the terminal.

**Requirements:**
* Python 2.7+
* MAMP/MAMP Pro
* Mac OSX 10.10

** Directions for use:**
1. Place script some where easily accessible via the terminal.
2. `cd` to the directory the script lives.
3. Run `sudo python local-dev.py`
4. Follow the on screen instructions.
	* **Only** enter the base domain for your local environment. The script will automatically add `.local` to the domain to create your local URL. We place alternate DNS rules in the `/etc/hosts` file to ensure there are no conflicts with OS X operations.
	* If you would like to install WordPress into your newly created environment, simply type `Y` when prompted.
5. Because this script was ran with `sudo` you will probably have to change ownership of the directory and files included.
