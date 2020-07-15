# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#Step 1
#Appending new_record to data
census = np.concatenate((data, new_record), axis=0)
print(data.shape)
print(census.shape)
print('_'*100)

#Step 2
#Extracting age column
age = census[:, 0]
#Max age
max_age = age.max()
print(max_age)
#Min age
min_age = age.min()
print(min_age)
#Mean age
age_mean = age.mean()
print(age_mean)
#Std age
age_std = np.std(age)
print(age_std)
print('_'*100)

#Step 3
race_0 = census[:, 2] == 0 
len_0 = len(census[race_0])
print(len_0)
race_1 = census[:, 2] == 1
len_1 = len(census[race_1])
print(len_1)
race_2 = census[:, 2] == 2
len_2 = len(census[race_2])
print(len_2)
race_3 = census[:, 2] == 3
len_3 = len(census[race_3])
print(len_3)
race_4 = census[:, 2] == 4
len_4 = len(census[race_4])
print(len_4)

#Race with min no. of citizens
minority_race = 3
print("Minority race is", minority_race)
print('_'*100)

#Step 4
#Is the govt policy followed?
senior_citizens = census[:, 0] > 60
working_hours_sum = census[:, 6][senior_citizens].sum()
print(working_hours_sum)
senior_citizens_len = len(census[senior_citizens])
print(senior_citizens_len)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)
print('_'*100)

#Step 5
high = census[:, 1] > 10
low = census[:, 1] <= 10
avg_pay_high = census[:, 7][high].mean()
print(avg_pay_high)
avg_pay_low = census[:, 7][low].mean()
print(avg_pay_low)



