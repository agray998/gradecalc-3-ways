def gradecalc(name: str, homework: int, assessment: int, exam: int) -> str:
    '''Calculates a percentage based on three marks, one out of 25,
    one out of 50 and one out of 100, and determines a grade (A* - D)
    based on this percentage.'''
    percent = int((homework + assessment + exam) * 100 / 175)
    grades = {100:'A*', 90:'A*', 80:'A', 70:'B', 60:'C', 50:'D'}
    gradebound = percent - (percent % 10)
    grade = grades.get(gradebound, 'F')
    return f"{name} scored {percent}%. {name}'s grade is {grade}"
