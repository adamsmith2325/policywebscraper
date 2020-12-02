import re

keywords=[
'State of Emergency', 
'Declared', 
'State of Emergency Declared', 
'Continuation of Emergency Declare', 
'Stay at Home', 'Curfew', 
'Mask',
'Masks',
'Mask Requirement',
'Mask Required',
'Buisness Closure',
'Essential Buisness',
'Gathering',
'Max',
'Social Distancing',
'CDC Guidelines',
'Guidelines',
'CDC',
'Restraunt Restrictions',
'Restrictions',
'Schools',
'School',
'School Closure',
'Medical Procedures',
'Medical',
'Travel Restrictions',
'Travel Ban',
'Travel',
'Jail',
'Correctional Facilities'
]
def readin(file)
    with open(file) as f:
        txt=f.read()
        for i in keywords:

            if re.search(r'\b{}\b'.format(i),txt):
                print(i)