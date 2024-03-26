import os, platform, random, re, subprocess

### CONFIG
elevate = "doas" # Change to sudo if you want.
wg_configs = ["de-fra-wg-008", "gb-lon-wg-204", "nl-ams-wg-102", "sg-sin-wg-001", "us-dal-wg-108", "us-nyc-wg-501", "us-slc-wg-101"] # List of wireguard names found from /etc/wireguard. Default is mullvad.
editor = "micro" # vim, nvim, nano, micro, emacs, mousepad etc
termcfg = "alacritty/alacritty.toml" # Terminator, kitty etc
###

if "Linux" not in platform.platform() and os.name == "posix":
    print("This script is designed for linux")
    raise Exception("Only works on Linux")

while True:
    command = input("$ ")
    if command == "vpn up":
        wg = random.choice(wg_configs)
        print("Starting up", wg)
        os.system(f"{elevate} wg-quick up {wg}")
    elif command == "vpn down":
        output = subprocess.run([elevate, 'wg', 'show'], capture_output=True, text=True)
        match = re.search(r'interface: (\S+)', output.stdout)
        if match:
            print("Brining down", match.group(1))
            os.system(f"{elevate} wg-quick down {match.group(1)}")
        else: 
            print("No active wireguard configuration")
    elif command == "vpn":
        output = subprocess.run([elevate, 'wg', 'show'], capture_output=True, text=True)
        match = re.search(r'interface: (\S+)', output.stdout)
        if match:
            print("Currently up:", match.group(1))
        else:
            print("No active wireguard configuration")
    elif command == "clear":
        os.system("clear")
    elif command == "exit":
        exit()
    elif command == "edit sway":
        os.system(f"{editor} ~/.config/sway/config")
    elif command == "edit term":
        os.system(f"{editor} ~/.config/{termcfg}")
    elif command == "ff":
        os.system("firefox & disown")
    elif command == "dsc":
        os.system("discord & disown")
    elif command == "code":
        os.system("vscodium & disown")
    elif command == "litexl":
        os.system("lite-xl & disown")
    elif command == "off":
        os.system("systemctl poweroff")
    elif command == "exit sway":
        os.system("swaymsg exit")
