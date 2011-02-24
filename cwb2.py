# Filename: web2.py
# Name: Zhong Jingjie
# Centre No / Index No: 3024/
# Description: Read from RESOURCE.DAT, get extra info based on resource type
#              Perform validation and write to URESOURCE.DAT

from classes import *
resource_list = []

def UPDATERESOURCE():

    try:
        # open resource file for reading
        resource_file = open("RESOURCE.DAT", "r")
        
        # open updated file for writing
        uresource_file = open("URESOURCE.DAT", "w")
        
        # read heading line from resource file (creation date + number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")

        # store creation date and number of records
        creation_date = heading_line[:10]
        num_recs = heading_line[10:]

        # write creation date and number of records to updated resource file
        uresource_file.write(creation_date + num_recs + "\n")

        # read remaining records
        detail_lines = resource_file.readlines()
        
        # loop for number of records
        for record_line in detail_lines:
            # clean record line
            record_line = record_line.rstrip("\n")

            # store resource number, title, date acquired and resource type
            resource_no = record_line[:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]
            
            # print resource info
            print("Resource no: " + resource_no)
            print("Title: " + title)
            print("Date Acquired: " + date_acquired)
            print("Resourc type: " + resource_type)
            
            # if resource type is music cd
            if resource_type == "C":
                # get and validate artist
                valid_artist = False
                while not valid_artist:
                    artist = input("Enter artist: ")
                    if len(artist) == 0: # presence digit
                        print("Invalid! Empty input. Try again.")
                    elif len(artist) > 50: # length check
                        print("Invalid! Artist name cannot exceed 50 characters. Try again.")
                    else:
                        valid_artist = True
                        
                # get and validate number of tracks
                valid_num_tracks = False
                while not valid_num_tracks:
                    num_tracks = input("Enter number of tracks: ")
                    if len(num_tracks) == 0:
                        print("Invalid! Empty input. Try again.")
                    elif not num_tracks.isdigit(): # data type check
                        print("Invlaid! Must be a number. Try again.")
                    elif not (0 < int(num_tracks) <= 20): # range check
                        print("Invalid! Number of tracks must be between 1 and 20. Try again.")
                    else:
                        valid_num_tracks = True

                # create music CD object and add to resource list
                resource_list.append(MusicCD(resource_no, title, date_acquired, resource_type, artist, num_tracks))
                    
            # else resource type is film dvd
            else:
                # get and validate director
                valid_director = False
                while not valid_director:
                    director = input("Enter director: ")
                    if len(director) == 0: # presence check
                        print("Invalid! Empty input. Try again.")
                    elif len(director) > 50: # length check
                        print("Invalid! Director name cannot exceed 50 characters. Try again.")
                    else:
                        valid_director = True

                # get and validate running time
                valid_running_time = False
                while not valid_running_time:
                    running_time = input("Enter Running Time: ")
                    if len(running_time) == 0: # presence check
                        print("Invalid! Empty input. Try again.")
                    elif not (30 <= int(running_time) <= 180):  #length check
                        print("Invalid! Running time must be between 30 to 180 minutes. Try again.")
                    elif not running_time.isdigit(): # data type check
                        print("Invalid! Running time must be a number. Try again.")
                    else:
                        valid_running_time = True
                
                # create film DVD object and add to resource list
                resource_list.append(FilmDVD(resource_no, title, date_acquired, resource_type, director, running_time))

        # write full resource details to updated resource file
        for resource in resource_list:
            uresource_file.write(resource.display() + "\n")
        # close files
        resource_file.close()
        uresource_file.close()

    except IOError:
        # display input / output error
        print("Error! Cannot read from input file or write to output file!")

# Main Program
if __name__ == "__main__":
    UPDATERESOURCE()
