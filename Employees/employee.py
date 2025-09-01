employees=[
    {'eid':101,'ename':'Rahul','gender':'Male'},
    {'eid':102,'ename':'Sonia','gender':'Female'},
    {'eid':103,'ename':'Priyanka','gender':'Female'},
]
#print employee names

for employee in employees:
    print("Employee Name:", employee['ename'])


#print no of male and female Employees from above source
no_of_male_employees=0
no_of_female_employees=0
for emp in employees:
    if emp['gender']=='Male':
        no_of_male_employees=no_of_male_employees+1
    if emp['gender'] =='Female':
        no_of_female_employees=no_of_female_employees+1

print("No of Male Emplyees:", no_of_male_employees)
print("No of Female Emplyees:", no_of_female_employees)