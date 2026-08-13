student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# sums up integers from list together
total_exam_score = sum(student_scores)

print(total_exam_score)

# same results using For loop
sum = 0
for score in student_scores:
    sum += score

print(sum)

# prints highest value in list
print(max(student_scores))

# same result using For loop
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)
