"""
This module is responsible for deal with student functionality
"""

student_table = {
    1: {'name': "Vinay", "dob": "2-3-1991", 'address': "Hyderabad"},
    2: {'name': "mahesh", "dob": "2-3-1993", 'address': "Hyderabad"},
    3: {'name': "sandhya", "dob": "2-3-1994", 'address': "Hyderabad"}
}

student_marks = {
    1: {'marks': 600},
    2: {'marks': 600},
}


def get_student_info(student_id):
    return student_table[student_id]

def get_student_marks(student_id):
    return student_marks[student_id]