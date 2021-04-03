from ConnectCouch import connectCouch

speaker = {
    "speaker_new" : {
        "seek" : "int",
        "volume" : "float",
        "play" : "boolean",
        "title" : "string"
    },
    "controls" : {
        "increaseVolume" : {
            "step" : "int",
            "mute" : "boolean"
        },
        "increaseSeek" : {
            "step" : "int"
        }
    }
}

s = {
    "sensorName" : "SensorName",
    "sensorid" : "sensorid",
    "sensorurl" : "<public-IP of intermediate server>",
    "Location" : "<A1:A2:A3....>",
    "sensorType" : "speaker"
}

print(connectCouch.sensorTypeRegistration(speaker))
print(connectCouch.SensorInstanceRegistration(s))