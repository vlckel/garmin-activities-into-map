####
####
## process all TXC files in a given folder. Extract longitude, latitude and type of sport and save it as csv file (so it can be later imported into GIS)

from xml.dom.minidom import parse
import xml.dom.minidom
import csv
import os

directory = r'C:/Users/elisk/Desktop/_git/garmin/TCX'

filenames = []
for filename in os.listdir(directory):
    if filename.endswith("tcx"):
        tcx_file = os.path.join(directory, filename)
        filenames.append(tcx_file)
        
#print(filenames)

for file in filenames:
    #print(file)
    csv_data = []

    xml_tree = xml.dom.minidom.parse(file)

    activities = xml_tree.documentElement.getElementsByTagName("Activities")[0]
    for activity in activities.getElementsByTagName("Activity"):
        sport = activity.getAttribute("Sport")
        laps = activity.getElementsByTagName("Lap")
        for lap in laps:
            track = lap.getElementsByTagName("Track")[0]
            for trackpoint in track.getElementsByTagName("Trackpoint"):
                print(trackpoint)
                position = trackpoint.getElementsByTagName("Position")
                if position:
                    print(position)                        
                    latitude = position.getElementsByTagNameNS("*", "LatitudeDegrees")[0]
                    longitude = position.getElementsByTagNameNS("*","LongitudeDegrees")[0]
                    csv_data.append([latitude, longitude, sport])


    with open(file + '.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(['latitude','longitude', 'sport'])
        for data in csv_data:
            csvwriter.writerow(data)
                    