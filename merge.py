import csv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

brightest_stars = []
brown_dwarfs = []

with open("brightest_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        brightest_stars.append(row)
    del brightest_stars["luminosity"]

with open("brown_dwarfs.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        brown_dwarfs.append(row)

brown_dwarfs = brown_dwarfs.rename({
    'constellation': 'const.'
}, axis = 'columns')

headers_1 = brightest_stars[0]
data_1 = brightest_stars[1:]

headers_2 = brown_dwarfs[0]
data_2 = brown_dwarfs[1:]

planet_masses = []
planet_radiuses = []
planet_names = []

for data in data_1:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])

planet_gravity = []

for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

headers = headers_1 + headers_2
data = []
for index, data_row in enumerate(data_1):
    data.append(data_1[index] + data_2[index])

temp_planet_data_rows = list(data)
for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    data.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []

for planet_data in data:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])

planet_gravity = []

for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

# Clustering 

X = []
for index, planet_mass in enumerate(planet_masses):
  temp_list = [
                  planet_radiuses[index],
                  planet_mass
              ]
  X.append(temp_list)

wcss = []
for d in range(1, 11):
    kmeans = KMeans(n_clusters=d, init='k-means++', random_state = 42)
    kmeans.fit(X)
    # inertia method returns wcss for that model
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='blue')
plt.title('Elbow Method')
plt.xlabel('# of clusters')
plt.ylabel('WCSS')
plt.show()

final_planet_list = []

for planet_data in planet_data_rows:
  temp_dict = {
                  "name": planet_data[1],
                  "distance_from_earth": planet_data[2],
                  "planet_mass": planet_data[3],
                  "planet_type": planet_data[6],
                  "planet_radius": planet_data[7],
                  "distance_from_their_sun": planet_data[8],
                  "orbital_period": planet_data[9],
                  "gravity": planet_data[20],
                  "orbital_speed": planet_data[21]
              }
  temp_dict["specifications"] = final_dict[planet_data[1]]
  final_planet_list.append(temp_dict)

print(final_planet_list)

with open("merge.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)