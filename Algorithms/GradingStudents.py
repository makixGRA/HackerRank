# Grading students

# https://www.hackerrank.com/challenges/grading/problem

# Author: Miguel Anguita


def gradingStudents(grades):
    new = []
    for i in grades:
        sum = i
        if(i < 38):
            new.append(i)
        else:
            while(sum % 5 != 0):
                sum += 1
            if((sum-i) < 3):
                new.append(sum)
            else:
                new.append(i)
    return new



if __name__ == '__main__':
    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
