# It is one of data structure of python used to group related piece of information together in the form of key value pair
# syntax:{key:value}
# eg
# prog_dic = {
#     "bug": "the error that prevent a code from running"
# }
# # accessing data from dictionary
# print(prog_dic["bug"])
# Checking the data type is also important

# Adding item to the list
# prog_dic["loop"] = "an instruction that tells the computer to execute the code again and again untill the condition fulfilled"
# print(prog_dic)

# # print the key using for loop
# for key in prog_dic:
#     print(key)
#     # print value of the key
#     print(prog_dic[key])

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
# Todo-1:Create an empty dictionary called student_grade
student_grades = {}
# Todo-2:Write code to add the grades
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 81:
        student_grades[key] = "Exceed Expectation"
    elif student_scores[key] > 71:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
print(student_grades)

# challenge-2:Dictionary in list
travel_log = [
    {
        "country": "france",
        "visits": 12,
        "cities": ["paris", "lille", "Dijon"]
    },
    {
        "country": "German",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# Write code here to insert


def add_new_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    return new_country


travel_log.append(add_new_country("Russia", 2, ["Moscow", "saint petersnurg"]))
print(travel_log)
