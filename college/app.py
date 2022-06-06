from college.student.student import *
from college.admin.fee import get_fee


out = get_student_info(2)
print(out)
marks = get_student_marks(2)
print(marks)



# get fee for year
fee = get_fee("first_year")
fee = get_fee("second_year")
print(fee)