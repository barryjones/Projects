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

# NAME,LEG_LENGTH,DIET 
# Hadrosaurus,1.2,herbivore 
# Struthiomimus,0.92,omnivore 
# Velociraptor,1.0,carnivore 
# Euoplocephalus,1.6,herbivore 
# Stegosaurus,1.40,herbivore 
# Tyrannosaurus Rex,2.5,carnivore"; 

# NAME,STRIDE_LENGTH,STANCE 
# Euoplocephalus,1.87,quadrupedal 
# Stegosaurus,1.90,quadrupedal 
# Tyrannosaurus Rex,5.76,bipedal 
# Hadrosaurus,1.4,bipedal 
# Struthiomimus,1.34,bipedal 
# Velociraptor,2.72,bipedal"; 


import math

dinosaurs = [
{'NAME':'Hadrosaurus', 'LEG_LENGTH':'1.2', 'DIET':'herbivore', 'STRIDE_LENGTH':'1.4', 'STANCE':'bipedal'},
{'NAME':'Struthiomimus', 'LEG_LENGTH':'0.92', 'DIET':'omnivore', 'STRIDE_LENGTH':'1.34', 'STANCE':'bipedal'},
{'NAME':'Velociraptor', 'LEG_LENGTH':'1.0', 'DIET':'carnivore', 'STRIDE_LENGTH':'2.72', 'STANCE':'bipedal'}, 
{'NAME':'Euoplocephalus', 'LEG_LENGTH':'1.6', 'DIET':'herbivore', 'STRIDE_LENGTH':'1.87', 'STANCE':'quadrupedal'}, 
{'NAME':'Stegosaurus', 'LEG_LENGTH':'1.40', 'DIET':'herbivore', 'STRIDE_LENGTH':'1.90', 'STANCE':'quadrupedal'}, 
{'NAME':'Tyrannosaurus Rex', 'LEG_LENGTH':'2.5', 'DIET':'carnivore', 'STRIDE_LENGTH':'5.76', 'STANCE':'bipedal'}
]

dinoSpeed = []

for i in dinosaurs:
	if i["STANCE"] == "bipedal":
		STRIDE_LENGTH = float(i["STRIDE_LENGTH"])
		LEG_LENGTH = float(i["LEG_LENGTH"])
		speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * 9.8)
		dinoSpeed.append({'NAME':i['NAME'], 'SPEED':speed})
		

print(dinoSpeed)

