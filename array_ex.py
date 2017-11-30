import numpy as np

weight = np.array([1,2,3])
height = np.array([10,20,30])

bmi = weight / height ** 2

print (bmi)

bmi_2 = bmi + bmi

print (bmi_2)

np_fam = np.array([[1,2,3],
                    [10,20,30]])

bmi_3 = np_fam[0]/(np_fam[1:,]**2)

print (bmi_3)
print (type(bmi_3))
print (bmi_3[:,2])
print (np_fam)  
print (type(np_fam))