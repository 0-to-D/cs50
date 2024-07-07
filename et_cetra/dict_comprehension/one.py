################################################
# list version

students = ["one","two","three"]

answer = [{"name":name, "house":"gryffendor"} for name in students]

print(answer)

###############################################
# dict version

answer1 = {name:"gryffendor" for name in students}
