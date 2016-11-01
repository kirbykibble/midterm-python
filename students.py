# students.py
#
# Author:  Dylan Chew
# BCIT ID: A00986529
# Set:     1B
# Date:    October 28th, 2016
#
# Description: Processes course and student grade data.
#
# Notes:   I couldn't get test 4a and the second line in verifying input was read to produce the correct output. Not entirely sure what the problem is.
#-------------------------------------------------------------------------
#
# Global Data Structures: DO NOT CHANGE; DO NOT ADD ANY MORE GLOBAL DATA STRUCTS
GR_DATA = [ "SN018569 BUS 172 Business 74 4",
            "SN018569 CMP 101 Computational Logic 89 4",
            "SN018569 CMP 102 Web Development 85 4",
            "SN018569 CMP 151 Programming 1 (Java) 79 7",
            "SN018569 ENG 101 Intro to Communications 66 4",
            "SN018569 MTH 101 Discrete Mathematics 61 4",
            "SN018569 PRJ 190 Practicum 81 6",
            "SN018569 SKL 001 Study Skills P 1",
            "SN415751 CMP 102 Web Development W 4",
            "SN415751 CMP 104 Programming 1 (Python) 80 3",
            "SN415751 CMP 105 Programming 1 (Javascript) 21 3",
            "SN415751 CMP 151 Programming 1 (Java) W 7",
            "SN415751 MTH 101 Discrete Mathematics W 4",
            "SN415751 PRJ 190 Practicum F 6",
            "SN415751 SKL 001 Study Skills F 1"
          ]

# Constants: ADD ADDITIONAL CONSTANTS AS NEEDED; DO NOT CHANGE THESE ONES
HC_STUDENT_1 = "SN018569"
HC_STUDENT_2 = "SN415751"
HC_STUDENT_3 = "SN464730"
HC_STUDENT_4 = "SN473939"
HC_STUDENT_5 = "SN728125"
COURSE1 = "CMP 151"
COURSE2 = "COP 200"
INP_FILE_01 = "StudentData.txt"
OUT_FILE_01 = "StudentRank(out).txt"


# Function Definitions: CODE THE FUNCTIONS HERE. You can add new helper
# functions as you require...

def get_student_list(): 
    #initiates a list
    unique_students = []
    
    #iterates through all students
    for items in GR_DATA: 
        items = items.split()
        if items[0] not in unique_students:
            unique_students.append(items[0])
        else:
            continue
    return(unique_students)

def reg_stats():
    #initiates a dict
    students_per_course = {}
    
    #iterates through courses and counts the number of students in each course
    for items in GR_DATA:
        items = items.split()
        course = ""
        course = course.join([items[1], " ", items[2]])
        if course not in students_per_course:
            students_per_course[course] = 1
        else:
            students_per_course[course] += 1
    return(students_per_course)

def calculate_gpa(students): 
    #initiates the gpa and total_credits
    gpa = 0
    total_credits = 0
    
    #iterates through each item, calculating the gpa at the end
    for items in GR_DATA:
        items = items.split()
        
        #checks for Failures, passes, or dropouts and acts accordingly
        if students == items[0]:            
            if items[-2] == "F":
                gpa += 0
                total_credits += int(items[-1])
            elif items[-2] == "P":
                gpa += (100 * int(items[-1]))
                total_credits += int(items[-1])
            elif items[-2] == "W":
                continue
            else:
                gpa += (int(items[-2]) * int(items[-1]))
                total_credits += int(items[-1])
    
    #makes sure that there isn't a divide by 0 error
    if total_credits > 0:
        gpa /= total_credits
        gpa = int(round(gpa, 0))
    return(gpa)
    
def import_grades(filename):
    #opens the file for reading and appends it to GR_DATA
    with open(filename, "r") as student_info:
        lines = student_info.read().splitlines()
        
        #adds lines if they don't exist
        for items in lines:
            if items not in GR_DATA:
                GR_DATA.append(str(items))
            else:
                continue
    return(GR_DATA)

def is_fulltime(stu_id): 
    #initiates credit and course counts
    credit_count = 0
    course_count = 0
    
    #iterates through the file and adds credits/course count accordingly
    for items in GR_DATA:
        items = items.split()
        if (items[0] == stu_id):
            course_count += 1
            credit_count += int(items[-1])
        else:
            continue
    
    #checks to make sure the course count and credit count are valid for fulltime status
    if (course_count >= 3) and (credit_count >= 15):
        full_time = True
    else:
        full_time = False
    return(full_time)


def print_student_rankings(filename):
    #creates the file for writing. If the file doesn't exist, it makes a new one. If it does, it replaces the old one.
    with open(filename, "w+") as student_rankings:
        #initiates a count, student ranking, and gets the list of students.
        position = 0
        student_rank = {}
        student_list = get_student_list()
        
        #calculates the gpa of each student and adds them to the dictionary
        for items in student_list:
            gpa = calculate_gpa(items)
            student_rank[gpa] = items
        
        #sorts the dictionary by ranking
        student_rank = sorted(student_rank.items(), reverse=True)
        
        #checks each student if they are fulltime or not
        for key, values in student_rank:
            fulltime_students = []
            fulltime = is_fulltime(values)

            #if fulltime, counts the position up by one and joins the values together.
            if fulltime == True:
                position += 1
                output = ""
                output = output.join([str(position), ". ", str(values), " ", str(key), "\n"])
                student_rankings.write(output)

    return(position)


##############################################################################
# Below is the main routine. It is a test driver. Do not modify or change 
# this function in any way. All your code will go above this section.
#
#         *** DO NOT CHANGE THE CODE IN MAIN ***
#
# Uncomment the lines by deleting "#--" after you have coded each function.
#
def main():
    # needed for local reassignment of GR_DATA in Test 4
    global GR_DATA

    ### EXERCISE 1a: code and test function get_student_list (see instructions)
    students = get_student_list()
    print("\nTest 1a:", sorted(students))
    
    ### EXERCISE 2a: code and test function reg_stats (see instructions)
    registrations = reg_stats()
    print("\nTest 2a:", registrations)
        
    ### EXERCISE 3a: code and test function calculate_gpa (see instructions)
    gpa1 = calculate_gpa(HC_STUDENT_1)
    gpa2 = calculate_gpa(HC_STUDENT_2)
    print("\nTest 3a:", gpa1, gpa2)

    ### EXERCISE 4a: read data from a file    (record type 1)
    GR_DATA = import_grades(INP_FILE_01)
    print("\nTest 4a: record 1 = [%s]" % GR_DATA[0] )
    print("Test 4a: record %d = [%s]" % (len(GR_DATA), GR_DATA[len(GR_DATA)-1]))

    ### EXERCISE 5a: output student rank list to a file
    print("\nTest 5a: is_fulltime(%s) -> %s" % (HC_STUDENT_1, is_fulltime(HC_STUDENT_1)))
    print("Test 5a: is_fulltime(%s) -> %s" % (HC_STUDENT_3, is_fulltime(HC_STUDENT_3)))
    print("Test 5a: is_fulltime(%s) -> %s" % (HC_STUDENT_4, is_fulltime(HC_STUDENT_4)))    

    ### EXERCISE 6a: output student rank list to a file
    cnt = print_student_rankings(OUT_FILE_01)
    print("\nTest 5a: %d records written to file %s" % (cnt, OUT_FILE_01) )

    ### COMPREHENSIVE FINAL TEST
    print("\nVerifying student list ...") 
    try: 
        students = sorted(get_student_list())
        print("   ->", len(students), students[0], students[len(students)-1])
    except:
        print("   -> *** Exercise 1: Not finished, or generates error (exception) ")  
    try:   
        print("Verifying registration stats ...") 
        registrations = reg_stats()
        print("   ->", len(registrations), registrations[COURSE1], registrations[COURSE2])
    except:
        print("   -> *** Exercise 2: Not finished, or generates error (exception) ")  
    try: 
        print("Verifying gpa calculations ...") 
        print("   ->", calculate_gpa(HC_STUDENT_1), calculate_gpa(HC_STUDENT_2), 
                       calculate_gpa(HC_STUDENT_3), calculate_gpa(HC_STUDENT_5) )
    except:
        print("   -> *** Exercise 3: Not finished, or generates error (exception) ")  
    try: 
        print("Verifying input was read ...") 
        GR_DATA = import_grades(INP_FILE_01)
        print(GR_DATA[0])
        print("   ->", len(GR_DATA), "records")
        print("   ->", GR_DATA[100])
        if GR_DATA[10][len(GR_DATA[10])-1] == "\n": print("   -> *** file input not stripped")
    except:
        print("   -> *** Exercise 4: Not finished, or generates error (exception) ")  
    try: 
        print("Verifying is_fulltime ...") 
        print("   ->", is_fulltime(HC_STUDENT_1), is_fulltime(HC_STUDENT_2), is_fulltime(HC_STUDENT_4))

    except:
        print("   -> *** Exercise 5: Not finished, or generates error (exception) ") 
    try: 
        print("Verifying output file ...") 
        myf=open(OUT_FILE_01, "r")
        print("   -> %s" % myf.readline().rstrip() )
        print("   -> %s" % myf.readline().rstrip() )
        print("   -> %s" % myf.readline().rstrip() )
        myf.close()
    except:
        print("   -> *** Exercise 6: Not finished, or generates error (exception) ")  
    print()
    return
    
main()    # run the main routine
#
##############################################################################
