import requests
import os

# Last Modified: 10/24/18
# Modified by: Matthew Compelube
# Created by: Matthew Compelube

os.getcwd()
#File location for stored parsing
os.chdir('C:\\Users\Matthew\Dropbox\Programming Projects')
#Html file to be stored for parsing
fileStorage = open("demo.txt", "w")
#File to write parsed data for database implimentation
databaseWrite = open("inject.txt", "w")
#Url that we want to parse
request = requests.get('https://its.humboldt.edu/classrooms/labs-softwarelist', stream=True)

fileStorage.write(request.text)
fileStorage.close()

fileRead = open("demo.txt", "r")

databaseWrite.write("Auto Generated! All changes will be overwritted\n")
databaseWrite.write("\n")

for x in fileRead:
    print(x)
    x.strip()
    #Grabs the Name of each program
    if x.strip() == "<td class=\"views-field views-field-title\" >":
        counter = 0
        databaseWrite.write("\n")
        databaseWrite.write("insert into a_table\n")
        databaseWrite.write("values\n")
        string = ""
        programName = fileRead.readline()
        for i in programName:
            if i == '"':
                counter += 1
            if (counter == 1 and counter != 2):
                if i != '/' and i != '"':
                    string+=str(i)
        string+=str(", ")
        databaseWrite.write(string)
    #Grabs the software version of each software set
    if x.strip() == "<td class=\"views-field views-field-field-software-version-num\" >":
        versionNumber = fileRead.readline()
        counter = 0
        string = ""
        for i in versionNumber.strip():
            if i == " ":
                counter += 1
            if counter < 1:
                string+=str(i)
        string+=str(", ")
        databaseWrite.write(string)
    #Grabs the operating system for each software set
    if x.strip() == "<td class=\"views-field views-field-field-platform\" >":
        platform = fileRead.readline()
        counter = 0
        string = ""
        for i in platform.strip():
            if i == " ":
                counter += 1
            if counter < 1:
                string+=str(i)
        string+=str(", ")
        databaseWrite.write(string)
    #Grabs the location of each software set
    if x.strip() == "<td class=\"views-field views-field-field-sc-location\" >":
        locations = fileRead.readline()
        counter = 0
        string = ""
        for i in locations.strip():
            if i == "<":
                counter += 1
            if counter < 1:
                string+=str(i)
        databaseWrite.write(string.strip())
        databaseWrite.write("\n")

databaseWrite.close()
fileRead.close()
