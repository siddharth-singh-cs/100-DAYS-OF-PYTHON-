student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
i=0
for score in student_scores:
    if(student_scores[i]>student_scores[i+1]):
        max=student_scores[i]
    else:
        max=student_scores[i+1]
       i++ 
print(max)