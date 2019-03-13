from influxdb import InfluxDBClient
import pandas as pd


class create_dbUI(object):

 def create_db(self):
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('demo')

    file_path = r'C:\Users\hp\Desktop\C2ImportCalEventSample.csv'
    csvReader = pd.read_csv(file_path)
    print(csvReader.shape)
    print(csvReader.columns)

    for row_index, row in csvReader.iterrows():
        tags = row[0]
        fieldValue = row[2]

        json_body = [{
            "measurement": "table7",
            "tags": {
                "Reference": tags
            },
            "fields": {
                "value": fieldValue
            }
        }]

        print(json_body)
        client.write_points(json_body)