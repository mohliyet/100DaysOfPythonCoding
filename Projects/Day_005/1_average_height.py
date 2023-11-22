# Input a Python list of student heights
student_heights = input("Write the heights separating by space:\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

cnt = 0
sum_of_heights = 0
for height in student_heights:
  sum_of_heights += height
  cnt +=1
average_height = round(sum_of_heights/cnt)

print(f'total height = {sum_of_heights}')
print(f'number of students = {cnt}')
print(f'average height = {average_height}')

