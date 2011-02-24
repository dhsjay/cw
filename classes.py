# Filename: classes.py
# Name: Zhong Jingjie
# Centre No / Index No: 3024/
# Description: Supporting classes for resource, music cd and film dvd

''' Super class Resource '''
class Resource():

    ''' Resource class constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo# __ in front makes data inacessible
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    ''' Resource number accessor '''
    def getResourceNo(self):
        return self.__ResourceNo

    ''' Title accessor '''
    def getTitle(self):
        return self.__Title

    ''' Date Acquired accessor '''
    def getDateAcquired(self):
        return self.__DateAcquired

    ''' Resource type accessor '''
    def getResourceType(self):
        return self.__ResourceType

    ''' Title modifier '''
    def setTitle(self, newTitle):
        self.__Title = newTitle
        
    ''' Date Acquired modifier '''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    ''' Resource type modifier '''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    ''' Helper function to display data '''
    def display(self):
        return("{0:5s}{1:30s}{2:6s}{3:1s}".format \
               (self.__ResourceNo, self.__Title, self.__DateAcquired, self.__ResourceType))


    
# Sub class MusicCD
class MusicCD(Resource):

    ''' MusicCD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks

    ''' Artist Accessor '''
    def getArtist(self):
        return ("{0:50s}".format(self.__Artist))

    ''' NoOfTracks Accessor '''
    def getNoOfTracks(self):
        return ("{0:2s}".format(self.__NoOfTracks))

    ''' Artist Modifier '''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    ''' NoOfTracks Modifier '''
    def setNoOfTacks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTacks
    

    ''' Helper function to display all data '''
    def display(self):
        return("{0:42s}{1:50s}{2:2s}{3:50s}{4:3s}".format(super().display(), self.__Artist, self.__NoOfTracks, "NULL", "000"))


# Sub class FilmDVD
class FilmDVD(Resource):

    ''' FilmDVD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime

    ''' Director Accessor '''
    def getDirector(self):
        return ("{0:50s}".format(self.__Director))

    ''' RunningTime Accessor '''
    def getRunningTime(self):
        return ("{0:3s}".format(self.__RunningTime))

    ''' Director Modifier '''
    def setDirector(self, newDirector):
        self.__Director = newDirector

    ''' RunningTime Modifier '''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime
    

    ''' Helper function to display all data '''
    def display(self):
        return("{0:42s}{1:50s}{2:2s}{3:50s}{4:3s}".format(super().display(), "NULL", "00", self.__Director, self.__RunningTime))

##r1 = Resource("00001", "Best of Super Junior", "090911", "C")
##r2 = Resource("00002", "Shaolin Temple", "121210", "D")
##
##print(r1.getResourceNo())
##print(r1.display())
##print(r1.setTitle("Hello SJ!"))
##print(r1.display())
##
##r3 = Resource("00003", "", "", "")
##r3.setTitle("Good Morning Shinee")
##r3.setDateAcquired("080810")
##r3.setResourceType("C")
##print(r3.display())
##
##
##cd1 = MusicCD("00004", "Michael Jackson Last Album", "050508", "C", "Michael Jackson", 10)
##
##print(cd1.getResourceNo()) # Inheritance example
##print(cd1.display()) # Overriding example
### print(cd1.__Title) # Information Hiding
##
##dvd1 = FilmDVD("00005", "Green Hornet", "030311", "D", "Jay Chou", 120)
##
##res_list = []
##res_list.append(cd1)
##res_list.append(dvd1)
##
##for item in res_list:
##    print(item.display()) # polymorphism
