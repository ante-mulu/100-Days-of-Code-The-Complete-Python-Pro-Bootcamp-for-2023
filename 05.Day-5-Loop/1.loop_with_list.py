alphabets = ['a', 'b', 'c']
# to print all items in the list we can we for loop
# for i in alphabets:
#     print(i)
# Challenge-1:Average Height
# sum = 0
# Student_Heights = input().split(" ")
# for n in range(0, len(Student_Heights)):
#     Student_Heights[n] = int(Student_Heights[n])
#     sum += Student_Heights[n]
# average = sum/len(Student_Heights)
# print(f"average: {average}")

student_scores = input().split(" ")
largest_num = int(student_scores[0])
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if (student_scores[n] > largest_num):
        largest_num = student_scores[n]
print(f"The highest score in a class is:{largest_num}")
