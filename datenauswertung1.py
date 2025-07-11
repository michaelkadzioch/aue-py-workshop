import json

def readSensorData(inputFile):
    try:
        open(inputFile, 'r')
    except FileNotFoundError:
        return ''
    else:
        with open(inputFile, 'r') as file:
            return file.read()
        
def convertSensorData(sensorDataString):
    sensorDataAsFloat = []
    for element in sensorDataString.split(';'):
        try:
            float(element)
        except:
            pass
        else:
            sensorDataAsFloat.append(float(element))
    return sensorDataAsFloat

def writeSensorDataAsJson(sensorDataJson, outputFile):
    with open(outputFile, 'w') as file:
        file.write(json.dumps(sensorDataJson))


def main():
    inputFile = 'test-files/sensordaten.txt'
    outputFile = 'json-files/sensorauswertung.json'
    calcSensorData = {}

    sensorData = convertSensorData(readSensorData(inputFile))

    calcSensorData['average'] = sum(sensorData) / len(sensorData)
    calcSensorData['max'] = max(sensorData)
    calcSensorData['min'] = min(sensorData)

    writeSensorDataAsJson(calcSensorData, outputFile)


if __name__ == "__main__":
    main()