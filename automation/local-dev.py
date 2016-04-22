#!/usr/bin/python

"""

A simple script to automate the setup of a local development environment
for Mac OSX running MAMP/MAMP PRO.

Will add the local host URl to the /etc/hosts file.
Will add the MAMP Virtual Host declaration in the /Applications/MAMP/conf/apache/extra/httpd-vhosts.conf file
Will create the local development directory in /Applications/MAMP/htdocs if it doesn't exist
Abililty to download the latest version of WordPress to the newly created directory

Does not currently work on non-linux operating systems.

Author: Tyler Bailey <tylerb.media@gmail.com>
Version: 1.1

"""

import sys, os, urllib2

cur_version = sys.version_info
wpurl = "https://wordpress.org/latest.zip"

# Main script execution
def main() :

    print_intro_credits()
    
    # Get the hostname from the user -- method is version dependent
    if cur_version == (3,2) :
        hostname = input('Enter the hostname: ')
        wp_setup = input('Is this a WordPress site? (Y/N): ')
    else :
        hostname = raw_input('Enter the hostname: ')
        wp_setup = raw_input('Is this a WordPress site? (Y/N): ')

    hostname = hostname.lower()

    # Create a local URL out of the hostname
    if '.' in hostname:
        local_url = hostname
        hostname = hostname.split('.', 1)[0].replace('.', '')
    else :
        local_url = hostname + ".local"

    # Update MAMP Virtual Hosts File
    if update_vhosts(local_url, hostname) == True :
        print '\n\n MAMP Virtual Host created... n\n'
        
        # Update MAC Local Hosts File
        if update_local_hosts(local_url) == True :
            print 'Local host file updated...\n\n'

            # Create local directory
            if create_local_directory(hostname) == True :
                print 'Local directory created...\n\n'

                # Do we want to install WordPress?
                if(wp_setup == "Y") :
                    if download_wp(hostname) == True :
                        print 'WordPress successfully installed...'

                # Notify of completion
                print 'Local development environment configuration complete.\n\nHappy coding!\n\n'


# Open the MAMP Virtual Host file and add the new local development URL
def update_vhosts(local_url, hostname) :
    if os.path.isfile('/Applications/MAMP/conf/apache/extra/httpd-vhosts.conf') :
        f = open('/Applications/MAMP/conf/apache/extra/httpd-vhosts.conf', 'a')
        f.write('\n' + '# Added by Python Script' + '\n')
        f.write('<VirtualHost *:80>\n')
        f.write('    DocumentRoot "/Applications/MAMP/htdocs/' + hostname + '"\n')
        f.write('    ServerName ' + local_url + '\n')
        f.write('    ServerAlias ' + local_url + '.*.xip.io\n')
        f.write('</VirtualHost>\n')
        f.close()
        
        return True
    else :
        print '\n\n' + 'Your MAMP Virtual Hosts file was not found...'
        return False


# Open the local hosts file and add the new hostname
def update_local_hosts(hostname) :
    if os.path.isfile('/etc/hosts') :
        f = open('/etc/hosts', 'a')
        f.write('::1 ' + hostname + '\n')
        f.write('fe80::1%lo0 ' + hostname + '\n')
        f.write('127.0.0.1 ' + hostname + '\n')
        f.close()

        return True
    else :
        print '\n' + 'Your local hosts file was not found...'
        return False

# Check if the local directory exists and create it if not
def create_local_directory(hostname) :
    if not os.path.exists('/Applications/MAMP/htdocs/' + hostname) :
        os.makedirs('/Applications/MAMP/htdocs/' + hostname)

    return True
        

# Download latest WP Version
def download_wp(hostname) :
    print "\n\n Downloading the lastest version of WordPress...\n\n"

    # Download file
    request = urllib2.urlopen(wpurl)
    
    # Save file
    if os.path.exists('/Applications/MAMP/htdocs/' + hostname) :
        output = open("/Applications/MAMP/htdocs/" + hostname + "/wordpress.zip", "w")
        output.write(request.read())
        output.close()

    return True
    


# Shameless self promotion... and some instructions
def print_intro_credits() :
    print "\n\n"
    print "####################################################\n"
    print "#        Brought to you with <3 by:                #\n"
    print "#   Tyler Bailey <tylerb.media@gmail.com>          #\n"
    print "####################################################\n\n"
    print "Enter the name of the local environment you want to create below.\n"
    print "If you are using *anything other* than '.local' for your domain you must\n"
    print "enter it along with the hostname i.e. yoursite.com, otherwise just 'yoursite' will work."
    print "\n\n\n"

    return


# Begin script execution on init
if __name__ == '__main__' :
    main()
