# python variable
name="Faraz"
age=20
height=5.7
is_student=True

print("Name",name)
print("Age",age)
print("Height",height)
print("Is student",is_student)

# now we have to check the datatypes 
print(type(age))
print(type(is_student))
print(type(name))
print(type(height))

# assigning multi variable
first_name, last_name="Faraz","farooqi"
print("Full name of Student is :",first_name,last_name )


# Python Variables
# This program covers different ways of using variables in Python


# 1. Basic variable declaration

name = "Faraz"
age = 20
height = 5.7
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# 2. Checking the data type of variables

print("\nData Types:")

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# 3. Assigning multiple variables

first_name, last_name = "Faraz", "Farooqi"

print("\nFull Name:", first_name, last_name)


# 4. Assigning the same value to multiple variables

a = b = c = 10

print("\nSame Value:")
print("a =", a)
print("b =", b)
print("c =", c)


# 5. Variables can be updated

age = 20

print("\nOriginal Age:", age)

age = 21

print("Updated Age:", age)


# 6. Using variables in calculations

marks1 = 85
marks2 = 90
marks3 = 78

total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

print("\nMarks:")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# 7. Variables can store the result of an expression

price = 500
quantity = 3

total_price = price * quantity

print("\nShopping:")
print("Price:", price)
print("Quantity:", quantity)
print("Total Price:", total_price)


# 8. Swapping two variables

x = 10
y = 20

print("\nBefore Swapping:")
print("x =", x)
print("y =", y)

x, y = y, x

print("After Swapping:")
print("x =", x)
print("y =", y)


# 9. Different types of values can be stored in variables

student_name = "Faraz"
student_age = 20
student_height = 5.7
student_passed = True

print("\nStudent Information:")
print(student_name)
print(student_age)
print(student_height)
print(student_passed)


# 10. Using variables inside a sentence

course = "BCA Data Science"
college = "Chandigarh University"

print("\nEducation:")
print("My name is", student_name)
print("I am studying", course)
print("My college is", college)
