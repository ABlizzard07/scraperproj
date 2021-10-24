import csv

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

with open("merge.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)