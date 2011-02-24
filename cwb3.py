# Filename: cwb3.py
# Author: Zhong Jingjie
# Center / Index No: 3024 /
# Description: Create Loan records and validate data

import datetime
import time

def CREATELOAN():

    try:
        # Open LOANRESOURCE.DAT for reading
        loan_file = open("LOANRESOURCE.DAT", "r")

        # Read resource details from file
        detail_lines_studentid = loan_file.readlines()

        # Initialise student ID list
        studentid_list = []

        # Loop through records from LOANRESOURCE.DAT
        for record in detail_lines_studentid:
            # slice to get student ID.
            studentid = record[5:10]
            
            # append resource no. to student ID list
            studentid_list.append(studentid)

    except IOError:
        print("Error! File cannot be opened!")

    try:
        # Open URESOURCE.DAT and loan file for reading
        uresource_file = open("URESOURCE.DAT", "r")
        
        # Read and skip first line
        heading_line = uresource_file.readline()
        
        # Read record details from file
        detail_lines = uresource_file.readlines() 
        
        # Initialise resource no. list and student ID list
        resourceno_list = []
        
        # Loop through records from URESOURCE.DAT
        for record in detail_lines:
            # slice to get resource no.
            resourceno = record[:5]
            
            # append resource no. to resource no. list
            resourceno_list.append(resourceno)
            
        # Open Loan file for append
        loan_file = open("LOANRESOURCE.DAT", "a")

        # Allowing multiple loans
        isLoaning = False
        while not isLoaning:
            # Get and validate resource no.
            valid_resource_no = False
            while not valid_resource_no:
                resource_no = input("Enter resource no: ")
                if len(resource_no) == 0: # presence check
                    print("Invalid! Input is empty. Please try again.")
                elif len(resource_no) != 5: # length check
                    print("Invalid! Resource no must be 5 digits long. Try again.")
                elif not resource_no.isdigit(): # data type check
                    print("Invalid! Resource no can only contain digits. Try again.")
                elif resource_no not in resourceno_list:
                    print("Invalid! Resource does not exist. Try again.")
                else:
                    valid_resource_no = True
                    
            # Get and validate student id
            valid_studentID = False
            while not valid_studentID:
                studentID = input("Enter student ID: ")
                if len(studentID) == 0: # presence check
                    print("Invalid! Input is empty. Try again.")
                elif len(studentID) != 5: # length check
                    print("Invalid! Student ID must be 5 characters long. Try again.")
                elif studentID[:1] != 'S': 
                    print("Invalid! Student ID must start with character 'S'. Try again.")
                elif not studentID[1:5].isdigit(): # data type check
                    print("Invalid! last 4 characters of student ID must be digits. Try again.")
                elif not studentid_list.count(studentID) < 3:
                    print("Invalid! Student has already a max of 3 resources on loan. Student is unable to loan anymore resources.")
                else:
                    valid_studentID = True
                    
            # Get and validate student name
            valid_studentName = False
            while not valid_studentName:
                studentName = input("Enter student name: ")
                if len(studentName) == 0: # presence check
                    print("Invalid! Input is empty. Try again.")
                elif len(studentName) > 30 : # length check
                    print("Invalid! Student name cannot be more than 30 characters long. Try again.")
                else:
                    valid_studentName = True
                    
            # Calculate and display Date due back
            currentDate = datetime.date.today()
            loanPeriod = datetime.timedelta(days=7)
            dateDue = currentDate + loanPeriod
            print("Due by: ", dateDue)

            # Create blank evaluation field
            evaluation = ""

            
            # write valid records into file
            loan_file.write("{0:5s}{1:5s}{2:30s}{3:11s}{4:50s}".format(resource_no, studentID, studentName, dateDue.strftime("%y%m%d"), evaluation) + "\n")

            # Check if student still wants to loan
            loaningStatus = input("Loan successful. Would you like to make another loan? (Y/N)")
            if loaningStatus == 'N':
                isLoaning = True
        
        # Close files
        uresource_file.close()
        loan_file.close()

    except IOError:
        print("Error! File cannot be created or opened!")

# Main program
if __name__ == "__main__":
    CREATELOAN()
