# Filename: cw1atest.py
# Author: Zhong Jingjie
# Centre No / Index No:
# Description: Get resource data from ocnsole, validate data and output to text file

import datetime

def ADDRESOURCE():
    try:
        # open file for writing
        resource_file = open("RESOURCE.DAT", "w")

        # get creation date
        CreationDate = datetime.date.today()

        # write creation date to file
        # String format time method: small d = dd, small m = mm, small y = yy, big y = yyyy
        resource_file.write(CreationDate.strftime("%d-%m-%Y"))

        # get and validate number of resources
        valid_NumberOfResources = False
        while not valid_NumberOfResources:
            NumberOfResources = input("Enter number of resources: ")
            if len(NumberOfResources) == 0: #presence check
                print("Number of resources cannot be empty. Please try again.")
            elif not NumberOfResources.isdigit(): # data type check
                print("Number of resources must be a number. Try again.")
            elif not 0 < int(NumberOfResources) <=99999: # range check
                print("Number of resources must be in the range 1 to 99999. Try again.")
            else: # valid
                calid_NumberOfResources = True

        # write number of resources to file
        resources_file.write(NumberOfResources + "\n")

        # loop to get resource details
        for record in range(int(NumberOfResources)):

            # get and validate ResourceNo
            valid_ResourceNo = False
            while not valid_ResourceNo:
                ResourceNo = input("Enter resource no: ")
                # presence check
                # data type check
                # length check
                # range check 00001 - 99999
                # in running order
                # else valid

            # get and validate Title

            # get and validate DateAcquired

            # get and validate ResourceType

            # write resource record to file
            resource.write(ResourceNo, Title, DateAcquired, ResourceType)

        # close the file (data may not be written to the disk if file is left unclosed)
        resource_file.close()

    except IOError:
        print("Unable to create or write to file.")
        
# main program
if __name__ == "__main__":
    ADDRESOURCE()
