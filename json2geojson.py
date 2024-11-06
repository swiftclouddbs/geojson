import json
import geojson

def convert_to_geojson(json_data):
  """Converts a JSON object containing latitude and longitude to GeoJSON.

  Args:
    json_data: A Python object representing the JSON data.

  Returns:
    A GeoJSON FeatureCollection object.
  """

  features = []
  for place in json_data['places']:
    feature = geojson.Feature(
      geometry=geojson.Point((place['longitude'], place['latitude'])),
      properties={'name': place['name']}
    )
    features.append(feature)

  feature_collection = geojson.FeatureCollection(features)
  return feature_collection

# Load your JSON data
with open('./1562map_places.json', 'r') as f:
  data = json.load(f)

# Convert to GeoJSON
geojson_data = convert_to_geojson(data)

# Write the GeoJSON to a file
with open('./1562map.geojson', 'w') as f:
  geojson.dump(geojson_data, f)
