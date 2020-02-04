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

# dinosaurs = [
# {'NAME':'Hadrosaurus', 'LEG_LENGTH':'1.2', 'DIET':'herbivore', 'STRIDE_LENGTH':'1.4', 'STANCE':'bipedal'},
# {'NAME':'Struthiomimus', 'LEG_LENGTH':'0.92', 'DIET':'omnivore', 'STRIDE_LENGTH':'1.34', 'STANCE':'bipedal'},
# {'NAME':'Velociraptor', 'LEG_LENGTH':'1.0', 'DIET':'carnivore', 'STRIDE_LENGTH':'2.72', 'STANCE':'bipedal'}, 
# {'NAME':'Euoplocephalus', 'LEG_LENGTH':'1.6', 'DIET':'herbivore', 'STRIDE_LENGTH':'1.87', 'STANCE':'quadrupedal'}, 
# {'NAME':'Stegosaurus', 'LEG_LENGTH':'1.40', 'DIET':'herbivore', 'STRIDE_LENGTH':'1.90', 'STANCE':'quadrupedal'}, 
# {'NAME':'Tyrannosaurus Rex', 'LEG_LENGTH':'2.5', 'DIET':'carnivore', 'STRIDE_LENGTH':'5.76', 'STANCE':'bipedal'}
# ]


str1 = """Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore"""

#str1 = str1.replace('\n','')

lines = str1.split('\n')
#print(lines)

dinosaurs = []

for line in lines:
	items = line.split(',')
	#print(items)
	
	dinosaurs.append({'NAME':items[0], 'LEG_LENGTH':items[1], 'DIET':items[2]})

print(dinosaurs)







str2 = """# NAME,STRIDE_LENGTH,STANCE 
# Euoplocephalus,1.87,quadrupedal 
# Stegosaurus,1.90,quadrupedal 
# Tyrannosaurus Rex,5.76,bipedal 
# Hadrosaurus,1.4,bipedal 
# Struthiomimus,1.34,bipedal 
# Velociraptor,2.72,bipedal"""





# dinoSpeed = []

# for i in dinosaurs:
# 	if i["STANCE"] == "bipedal":
# 		STRIDE_LENGTH = float(i["STRIDE_LENGTH"])
# 		LEG_LENGTH = float(i["LEG_LENGTH"])
# 		speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * ((LEG_LENGTH * 9.8)**(1/2))
# 		dinoSpeed.append({'NAME':i['NAME'], 'SPEED':speed})
		

#print(dinoSpeed)
