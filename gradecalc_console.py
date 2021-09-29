from gradecalc import gradecalc

student_name = input("Please enter your name: ")
homework_score = int(input("Please enter your homework score (/25): "))
assessment_score = int(input("Please enter your assessment score (/50): "))
exam_score = int(input("Please enter your exam score (/100): "))

print(gradecalc(student_name, homework_score, assessment_score, exam_score))