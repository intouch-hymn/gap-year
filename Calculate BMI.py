#BMI calculate program
#BMI = weight(kg)/ height * height (m)

#input / convert str to int
weight = int(input('Please insert your weight (kg) :')) 
height = int(input('Please insert your height (cm):'))


#process
#cm->m
height /= 100
bmi = weight/height**2 #calculate BMI

#output
print('BMI = ',bmi)