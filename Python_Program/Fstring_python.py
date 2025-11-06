name = "prince"
age = 20
language = "python"
hours = 3

print(name, "is", age, "years old. He studies", language,hours,"hours a day.")

#using f-string
print(f"{name} is {age} year old. He studies {language} {hours} hours a day.")


sub1 = 70
sub2 = 80
sub3 = 90

print(f"{name} scored {sub1+sub2+sub3} marks in total.")

percent = (sub1+sub2+sub3)/3
print(f"{name} got {percent}%.")