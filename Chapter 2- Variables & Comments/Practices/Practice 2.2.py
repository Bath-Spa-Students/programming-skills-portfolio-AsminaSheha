'''Write a python program that takes courses marks as input and then calculates average of all the
courses. After calculating the average, calculate the percentage of a student using total marks. Assume
the total of all the courses marks is 500 or take the total marks from the user as input.'''

# Taking input for the number of courses
num_courses = int(input("Enter the number of courses: "))

# Taking input for total marks
total_marks = int(input("Enter the total marks: "))

# Initializing the sum of marks variable
sum_marks = 0

# Taking input for marks of each course
for i in range(num_courses):
    marks = int(input(f"Enter the marks for course {i+1}: "))
    sum_marks += marks

# Calculating the average
average_marks = sum_marks / num_courses

# Calculating the percentage
percentage = (sum_marks / total_marks) * 100

# Printing the average and percentage
print(f"The average marks is: {average_marks}")
print(f"The percentage is: {percentage}%")