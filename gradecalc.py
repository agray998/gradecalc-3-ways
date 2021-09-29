def gradecalc(name, homework, assessment, exam):
    percent = int((homework + assessment + exam) * 100 / 175)
    grades = {100:'A*', 90:'A*', 80:'A', 70:'B', 60:'C', 50:'D'}
    gradebound = percent - (percent % 10)
    grade = grades.get(gradebound, 'F')
    return f"{name} scored {percent}%. {name}'s grade is {grade}"
