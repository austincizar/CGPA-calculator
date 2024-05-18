
def CGPAcalculator():
    numberOfCourses = int(input("Input total number of courses offered in this semester: "))
    TCU = 0
    TQP = 0
    CGPA = 0
    
    for x in range(numberOfCourses):
        coursecode= input("Input course code: ")
        CU = int(input("Input course unit: "))
        TCU += CU
        grade = input("Input grade: ")
        print("*****************************************************************************************")
        if grade == "A":
            GP = 5
        elif grade == "B":
            GP = 4
        elif grade == "C":
            GP = 3
        elif grade == "D":
            GP = 2
        elif grade == "E":
            GP = 1
        else:
            GP = 0
            

        QP = GP * CU
        TQP += QP
        if x == (numberOfCourses-1):
            CGPA = round((TQP / TCU), 2)
            print("Your CGPG is: ", CGPA)
        
        
CGPAcalculator()