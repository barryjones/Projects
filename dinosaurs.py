# you will be supplied with two data files in CSV format. The first file contains 
# statistics about various dinosaurs. The second file contains additional data. 
# 
# Given the following formula, 
# 
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) 
# Where g = 9.8 m/s^2 (gravitational constant) 
# 
# Write a program to read in the data files from disk, it must then print the names 
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information. 

str1 = """Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore"""

str2 = """Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal"""

dinosaurs = dict()

# 'read in' first sting and put into datastructure
lines = str1.split('\n')

for line in lines:
	items = line.split(',')	
	dinosaurs[items[0]] = {
		'LEG_LENGTH':items[1],
		'DIET':items[2]
	}

# 'read in' second string and append to datastructure
lines = str2.split('\n')

for line in lines:
	items = line.split(',')
	dinosaurs[items[0]]['STRIDE_LENGTH'] = items[1]
	dinosaurs[items[0]]['STANCE'] = items[2]

# workout speed of bipedal dinosaurs and put into list
bipedalDinosaurs = []

for name in dinosaurs:
	if dinosaurs[name]['STANCE'] == "bipedal":
		
		STRIDE_LENGTH = float(dinosaurs[name]['STRIDE_LENGTH'])
		LEG_LENGTH = float(dinosaurs[name]['LEG_LENGTH'])
		speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * ((LEG_LENGTH * 9.8)**(1/2))

		bipedalDinosaurs.append([name,speed])

# sort fastest to slowest
bipedalDinosaurs.sort(key=lambda x: x[1], reverse=True)

# print only the names
for i in bipedalDinosaurs:
	print(i[0])


