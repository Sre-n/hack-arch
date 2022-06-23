import os
import gmaps
gmaps.configure(api_key=os.environ["GOOGLE_API_KEY"])

import gmaps
import gmaps.datasets
gmaps.configure(api_key='AI...') # Fill in with your API key
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
earthquake_df.head()

locations = earthquake_df[['latitude', 'longitude']]
weights = earthquake_df['magnitude']
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig
heatmap_layer = gmaps.heatmap_layer(locations)
heatmap_layer.point_radius = 8
heatmap_layer = gmaps.heatmap_layer(locations, point_radius=8)

import gmaps.datasets
rows = gmaps.datasets.load_dataset('gini') # 'rows' is a list of tuples
country2gini = dict(rows) # dictionary mapping 'country' -> gini coefficient
print(country2gini['United Kingdom'])

from matplotlib.cm import viridis
from matplotlib.colors import to_hex
# We will need to scale the GINI values to lie between 0 and 1
min_gini = min(country2gini.values())
max_gini = max(country2gini.values())
gini_range = max_gini - min_gini
def calculate_color(gini):
"""
Convert the GINI coefficient to a color
"""
# make gini a number between 0 and 1
normalized_gini = (gini - min_gini) / gini_range
# invert gini so that high inequality gives dark color
inverse_gini = 1.0 - normalized_gini
# transform the gini coefficient to a matplotlib color
mpl_color = viridis(inverse_gini)
# transform from a matplotlib color to a valid CSS color
gmaps_color = to_hex(mpl_color, keep_alpha=False)
return gmaps_color

colors = []
for feature in countries_geojson['features']:
country_name = feature['properties']['name']
try:
gini = country2gini[country_name]
color = calculate_color(gini)
except KeyError:
# no GINI for that country: return default color
color = (0, 0, 0, 0.3)
colors.append(color)

fig = gmaps.figure()
gini_layer = gmaps.geojson_layer(
countries_geojson,
fill_color=colors,
stroke_color=colors,
fill_opacity=0.8)
fig.add_layer(gini_layer)
fig
