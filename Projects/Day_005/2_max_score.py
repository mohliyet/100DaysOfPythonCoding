# Input a list of student scores
student_scores = input("Enter the list of scores:\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  
max_score = 0
for student_score in student_scores:
  if student_score > max_score:
    max_score = student_score

print(f'The highest score in the class is: {max_score}')
