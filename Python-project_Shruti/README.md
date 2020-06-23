### Project Overview

 The project include to create different dictonieries and list - concate the list, add or remove new values according to the situation and do the mathmetical operations(like percentage,maximum etc.) on it. And along with that do the operation on key - value pair of dictiniory such as converting the case of the key which is having macimum value.


### Learnings from the project

 Two ways to do the operation on key - value pair of dictiniory such as converting the case of the key which is having macimum value.
1- d=(courses.values())
max_d = max(d)
print(list(courses.keys())[list(courses.values()).index(max_d)])

2- by using max and dictionary name.get()


### Approach taken to solve the problem

 I have followed the problem step by step.
first ceating 2 list with different names and then create another variable in that store the concated list.
Remove the element and the corrected element.
create dictionary and found the total of it's values by using sum function.
create another variable(b) to store the length of keys (or total number of key,value pair)
and then find the percentage by total/b
and to find the key with the max value in a dictionary i have found the maximum values then passed that value to the index of values and print the corresponding key value.
And by using split function i have splitted it about space and stored as 2 different variable names and then concat these variables and then change the case to upper case by using upper().



### Challenges faced

 As max function wasn't iteratble with the indexed used on max value so i have followed below steps-
instead of direct writing the maximum function inside index, i have founded the maximum value and stored in a variable and passed directly that variable in index function
d=(courses.values())
max_d = max(d)
print(list(courses.keys())[list(courses.values()).index(max_d)])


### Additional pointers

 Try to come with another way instead of directly following the approach given in the task.


