import subprocess

interface = raw_input('Interface: ')
new_mac = raw_input('New MAC address: ')

print(f"[!] Changing MAC address for {interface} to {new_mac}")

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])