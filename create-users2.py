#!/usr/bin/python3

# INET4031
# Your Name: Bhumir Petel
# Data Created: 03/23/2025
# Date Last Modified: : 03/23/2025

#OS (interface with the OS), Re (parsing the input file), and Sys (system paramters such as exit) are phyton modules needed for this script to function
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    # adding prompt for user decide run the script in dry run move
    user_input = input("Test script in dry-run mode y or n?: ")
    dry_run = user_input.strip().lower() == 'y'

    for line in sys.stdin:
        #line = line.rstrip('\n')
        
        #Its reach for the "#" it its a indicate that the line "user" should not be added and skipped. if dry run prints notice there is comment to skip
        if re.match("^#", line):
            if dry_run:
                print("dry-run: skipping comment line #:")
            continue
        
        #The this parsing the line that is ":" deliminited to for the input line each field has particular value such as username, passsword, lastname, firstname, group
        fields = line.strip().split(':')
        
        #this is if check if there are not five fiels or "#" skip the line and go to next line as if there are not correct ammount of fields the script will error and is its "#" user does should not be added.   if dry run prints notice there is lien does not fit line format.
        if len(fields) != 5:
            if dry_run:
                print("dry-run: error - line does not match required format five feilds")
            continue

        #its setting the up the /etc/passwd file with the user name, password, last name, and first name
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        #its being split with "," as a user can be part of multiple groups
        groups = fields[4].split(',')

        #letting the you know which user will be created ie the current task of the script, the dry-run will output the command
        print("==> Creating account for %s..." % (username))
        #its using cmd from os module to run the add user command on the OS like it would be done manually, but without setting the password.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        if dry_run:
            print("Dry-run: Would run command /usr/sbin/adduser --disabled-password --gecos"
        else:
            #print cmd
            os.system(cmd)

        #letting the you know which user's password will be created ie the current task of the script, the dry-run will output the command
        print("==> Setting the password for %s..." % (username))
        #its using cmd from os module to run the add password command on the OS like it would be done manually 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        if dry_run:
            print("Dry-run: Would run command /bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s:"
        else:
            #print cmd
            os.system(cmd)

        for group in groups:
            #if there is no "-" value in the grup field add the user to the group otherwise move on to the next line". the dry-run will output the command
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                if dry_run:
                    print("Dry-run: Would run command cmd = /usr/sbin/adduser %s %s")
                else:
                    #print cmd
                    os.system(cmd)

if __name__ == '__main__':
    main()