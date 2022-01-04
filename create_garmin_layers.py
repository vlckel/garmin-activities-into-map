import arcpy, os
import pandas as pd

# Set environment settings

arcpy.env.workspace = r"C:/Users/elisk/Desktop/EfoxMaps/Garmin_Activities/garmin.gdb" #set the geodatabase you want to save the activities to
arcpy.env.overwriteOutput=True

# Set the local variables
in_folder = r"C:/Users/elisk/Desktop/EfoxMaps/Garmin_Activities/processed_txcs" #folder with saved csv files

x_coords = "longitude"
y_coords = "latitude"
z_coords = ""


#grab all the text files and put them in  a list
text_file_list = [ ]

for file in os.listdir(in_folder):
    if ".csv" in file:
        text_file_list.append(file)

path_list = [ ]
for text_file in text_file_list:
    
    in_table = os.path.join(in_folder,text_file)
    
    record = pd.read_csv(in_table)
    activity = (record['sport'].unique())
    
    name = text_file.strip(".tcx.csv")
    XYoutfc = os.path.join("in_memory",name)
    
    
    #check the activities with no coordinates (e.g. pool swimming)
    check_coords = (record['latitude'].unique())
    
    # create layers from activities with coordinates only
    if len(check_coords) != 0 :
        print(name)
        layer_xy = arcpy.management.XYTableToPoint(in_table, XYoutfc, x_coords, y_coords, z_coords, arcpy.SpatialReference(4326))
    
        layer_line = arcpy.PointsToLine_management(layer_xy,"line"+name,"", "")
        arcpy.AddField_management(layer_line, "activity", "TEXT", "", "", "", "", "", "", "")
        arcpy.Delete_management(layer_xy)
        field = ['activity']

        with arcpy.da.UpdateCursor(layer_line,field) as cursor:
            for row in cursor:
                row = activity
                cursor.updateRow(row)

        path_list.append(layer_line)

# merge all activities from the geodatabase into one layer
arcpy.Merge_management(path_list,"all_activities")

    

arcpy.Delete_management("in_memory")
        