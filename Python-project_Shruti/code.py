# --------------
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = [ 'Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2
new_class.append('Peter Warden')
new_class.remove('Carla Gentry')
print(new_class)

courses = {'Math': 65, 'English': 70, 'History': 80, 'French':70, 'Science': 60}
total = sum(courses.values())
print(total)
b= courses.keys()
a= len(b)
percentage = total/a
print(percentage)
 
d=(courses.values())
max_d = max(d)
print(list(courses.keys())[list(courses.values()).index(max_d)])

mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka': 65,'Yoshua Bengio':50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}
topper_1 = (mathematics.values())
max_topper_1 = max(topper_1)
maths_topper = (list(mathematics.keys())[list(mathematics.values()).index(max_topper_1)])
print(maths_topper)

f= maths_topper.split(' ')
first_name = f[0]
last_name = f[1]
full_name = last_name + ' ' + first_name
certificate_name = full_name.upper()
print(certificate_name)











