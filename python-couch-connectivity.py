import couchdb  # importing couchdb 

class ConnectCouch(object):
    def __init__(self):
        # Connecting with couchdb Server  
        self.database = couchdb.Server("http://admin:1234@127.0.0.1:5984/")
        self.sensorDatabase = self.database["sensor_database"]
        self.SensorTypesNames = "dfd681d1289db7ac36516b0b1c0008dc"
        self.SensorInstance = "dfd681d1289db7ac36516b0b1c0032e7"

    def RefreshValues(self):
        self.sensorDatabase = self.database["sensor_database"]
        self.SensorTypesNames = sensorDatabase["dfd681d1289db7ac36516b0b1c0008dc"]
        self.SensorInstance = sensorDatabase["dfd681d1289db7ac36516b0b1c0032e7"]

    def GetAllSensorTypes(self):
        return SensorTypesNames.keys()


    def Registration(self, sensorInstance, sensorTypeName):
        """
        Assuming that the SensorInstance and SensorTypeName are json Files
        """

        # Refesh values
        self.RefreshValues()

        # Check if the sensor type name exists
        sensorTypesPresent = self.GetAllSensorTypes()
        if()


# Creating Database
db = database["sensor_database"]

sensor_types_to_id_map_id = "dfd681d1289db7ac36516b0b1c0008dc"
sensor_ids_to_value_id = "dfd681d1289db7ac36516b0b1c0032e7"

sensor_type_to_id = db[sensor_types_to_id_map_id]

all_sensor_types = sensor_type_to_id.keys()
sensor_type_to_id.pop("_id")
sensor_type_to_id.pop("_rev")

for sensorTypes in  all_sensor_types:
    print(sensor_type_to_id[sensorTypes])