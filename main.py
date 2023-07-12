#  Print the average of the marks array for the student name provided, showing 2 places after the decimal.

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
sum = 0
count = 0
for name,score in student_marks.items():
    if query_name == name:
        for i in score:
            sum = sum + i
            count = count + 1

average = sum/count
print(format(average, ".2f"))