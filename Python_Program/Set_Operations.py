student1 = {"English", "Maths", "History", "Science", "cs", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics", "cs"}

# common subjects of student1 and student 2 - intersection
common_subjects = student1 & student2
print(common_subjects)

student1 = {"English", "Maths", "History", "Science", "cs", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics", "cs"}

# all subject of student1 and student2 - union

all_subjects = student1.union(student2)
print(all_subjects)

days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun"}
weekends = {"sat", "sun"}

# difference of sets
weekdays = days - weekends
print(weekdays)

weekends = days.difference(weekends)
print(weekends)