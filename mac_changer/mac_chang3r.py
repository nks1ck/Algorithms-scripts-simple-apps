import subprocess
import optparse # For user arguments 


def change_mac(interface, new_mac):
    '''Change MAC address'''
    print(f"[!] Changing MAC address for {interface} to {new_mac}")

    '''
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])
    '''


def get_arguments():
    '''Get arguments from user'''
    parser = optparse.OptionParser()

    # Interface help
    parser.add_option('-i', '--interface', dest='interface', help='The interface for which you need to change the MAC address')
    # MAC help
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')

    if options.interface:
        parser.error('[!] Please specify an interface, use --help for more information.')
    elif not options.new_mac:
        parser.error('[!] Please specify a new MAC adress, use --help for more information.')

    return options


options = get_arguments()
change_mac(options.interface, options.new_mac)
