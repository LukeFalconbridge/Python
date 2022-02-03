from re import A


name = input(str("please enter students name: "))
hws = input("please enter the students homework score: ")
assess = input("please enter the students assement score: ")
exam = input("pleaes inseert the students exam score: ")

hws = float(hws)
assess = float(assess)
exam = float(exam)

def grading(hws, assess, exam):
    hs = (hws/25)
    ams = (assess/50)
    es = (exam/100)
    grade = (hs*ams*es)*100
    return grade
score = grading(hws, assess, exam)
if score >= 65:
    gra = "B"
    if score >= 85:
        gra = "A"
elif score >= 50:
    gra = "C"
else:
    gra = "F"

print(name+"s graded score is", score,"%",gra)