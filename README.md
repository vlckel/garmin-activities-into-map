# garmin-activities-into-map
download all garmin activities and process them

- 1. download garmin activities
Use the script from Aneel Nazareth. With all the description how to use it at following link: https://wanderingstar.github.io/2018/01/21/13-08-bulk-download-garmin-connect-gpx.html

- 2. the script will download all activities in TCX format. In order to extract latitude, longitude and type of sport from that, run the "process_TCXfiles" script. 

- 3. "create_garmin_layers" is script which can be used for transforming all previously exported CSV files into separate layer within geodatabase in ArcGIS. Finally, it merges all the activity lines into one feature and keep the attributes at they were.
