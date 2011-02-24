# Filename: cwb4.py
# Author: Zhong Jingjie
# Centre / Index No: 3042 /
# Description: Create code to generate report that displays a list of resources
#               on loan, grouped by date due back.

import time
import datetime

def PRINTRECORD():

    try:
        # Open resource file for input
        resource_file = open("RESOURCE.DAT", "r")
        
        # Open loan file for input
        loan_file = open("LOANRESOURCE.DAT", "r")


        # Initialise loaned resource no list
        loanedResource_list = []

        # Initialise dictionary
        loanedResource_dict = {}
        
        # Read details from loan file and from resource file
        loan_details = loan_file.readlines()
        
        for record in loan_details:
            # Slice individual information from lines
            resourceNo = record[:5]
            studentID = record[5:10]
            studentName = record[10:40]
            dueDate = record[40:46]
            evaluation = record[46:96]
            # If resource is still on loan,
            if evaluation == (50*" "):
                # Format date
                dueDate = dueDate.datetime.strptime(dueDate, "%d%m%y")
                print(dueDate)
                # Append information
                loanedResource_list.append([resourceNo, dueDate, studentID, studentName])

        # Read details from resource file
        first_line = resource_file.readline()
        resource_details = resource_file.readlines()
        for record in resource_details:
            # Slice individual information from lines
            resourceNumber = record[:5]
            title = record[5:30]
            resourceType = record[41:]
            for i in range(0, len(loanedResource_list)):
                # If resource no matches one in the loanedResource_list, append title and resourceType to loanedResource_list record
                if resourceNumber == loanedRseource_list[i][0]:
                    if resourceType == 'C':
                        resourceType = "CD"
                    elif resourceType == 'D':
                        resourceType = "DVD"
                    loanedResource_list[i].append(title, resourceType)
                    break

        # Fill dictionary with key values as dueDates to get rid of duplicated dueDates
        for i in range(0, len(loanedResource_list)):
            loanedResource_dict[loanedResource_list[i][1]] = []

        # Get first and last date and format it


        # Append resource details to dictionary according to dateDue

        # Initialise date count as the first date

        # 
            
        


            
            
                
        
        # Close files

    except IOError:
        print("Error! Unable to create or open file!")

# Main program
if __name__ == "__main__":
    PRINTRECORD()
