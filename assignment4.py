from operator import itemgetter
def histogram(l1):
    l=l1[:]
    hist=[]
    while len(l)>0:
        element = l[0]
        m = 0
        for match in l:
            if element == match :
                m += 1
        hist.append((element, m))
        l = [x for x in l if x!=element]
        #print (l,id(l))
    hist = sorted(hist, key = itemgetter(1,0))
    return (hist)



def transcript(coursedetails,studentdetails,grades):
    studentgrades=[]
    for student in studentdetails:
        #print(student)
        rollnumber = student[0]
        name = student[1]
        coursedata=[]
        for coursegrade in grades:
            if coursegrade[0] == rollnumber:
                for course in coursedetails:
                    if coursegrade[1] == course[0]:
                        coursename = course[1]
                        coursedata.append((coursegrade[1],coursename,coursegrade[2]))
            coursedata = sorted(coursedata, key = itemgetter(0))
        studentgrades.append((rollnumber,name,coursedata))
    studentgrades = sorted(studentgrades, key = itemgetter(0))
    return (studentgrades)


    
