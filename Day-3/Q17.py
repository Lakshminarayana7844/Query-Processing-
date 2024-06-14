import pandas as pd

# Creating DataFrame
data = {'school': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
        'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
        'date_of_birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
        'age': [12, 12, 13, 13, 14, 12],
        'height': [173, 192, 186, 167, 151, 159],
        'weight': [35, 32, 33, 30, 31, 32],
        'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
        'school_code': ['$2', '$3', '$4', '$1', '$2', '$4']}

df = pd.DataFrame(data)

# Grouping by school code and calculating mean, min, and max age
result = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

print(result)
