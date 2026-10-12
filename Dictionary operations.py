student={"Roll":55,"Name":"Dharani","Course":"MCA"}
print(student["Name"])
print(student["Course"])
student["Department"]="CA"
student["CGPA"]=9.0
print(student)
student["CGPA"]=9.2
print(student)
del student["CGPA"]
print(student)
