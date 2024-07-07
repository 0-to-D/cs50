########################################
#old approach

student_list =["one","two","three","four\n\n\n"]

for i in range(len(student_list)):
    print(i+1, student_list[i])

###########################################

# using enumerate

for i,student in enumerate(student_list):
    print(i+1, student)

