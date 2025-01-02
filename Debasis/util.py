import pandas as pd
import json

def json_to_df(json_data):
  records = []
  for item in json_data:
    for point in item.get('points', []):
      record = {
        'location_x': point.get('location', {}).get('x', None),
        'location_y': point.get('location', {}).get('y', None),
        'location_z': point.get('location', {}).get('z', None),
        'transformation': point.get('transformation', None),
        'instance_id': point.get('instance_id', None)
      }

      records.append(record)

  return pd.DataFrame(records)


def read_json(json_path):
  with open(json_path, 'r') as file:
    data = json.load(file)

  return data