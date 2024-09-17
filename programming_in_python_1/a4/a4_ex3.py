def grade_calculator(
            assignments: list,
            bonus_assignment: int,
            exam: int) -> tuple[bool, int]:
    
    fail_pass = False
    grade = 0
    grade_max = 1100 if bonus_assignment != None else 1000
    assignments.append(bonus_assignment) 
    max_failed_assn = 4 

    if exam == None or exam < 50: # CASE C for failed exam 
        score_tuple = (False, 5)
        return score_tuple
        
    for assignment in assignments: 
        if assignment == None or assignment < 25: # CASE A for less than 25% in assignments 
            max_failed_assn -= 1
            if max_failed_assn == 0:
                score_tuple = (False, 5)
                return score_tuple
            
        if assignment != None:
            grade+=assignment

    if grade < grade_max/2: # CASE B for less than 50% in just the assignments 
        score_tuple = (False, 5)
        return score_tuple

    grade += exam
    percents = (grade/1100)*100
    print(percents)

    if percents >= 87.5:
        grade = 1
        fail_pass = True
    elif percents >= 75:
        grade = 2
        fail_pass = True
    elif percents >= 62.5:
        grade = 3
        fail_pass = True
    elif percents >= 50:
        grade = 4
        fail_pass = True
    else:
        grade = 5
        fail_pass = False

    score_tuple = (fail_pass, grade)
    return score_tuple


a9 = 98 #this is mininimum what u need for a 1 with 87.5 on exam
a10= 0 #+ this is min with 50 on exam
#total 95 to ensure 1 
print(grade_calculator([100,100,100,100,93,125,100,100,a9,a10], None, 50))



