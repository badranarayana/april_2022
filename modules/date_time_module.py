from datetime import date, timedelta, datetime



#date = "10-03-1991"
#date2 = "10-03-2022"


date1 = date(year=1991, month=3, day=10)
date2 = date(year=2022, month=3, day=10)


# delta between two days

out = date2 - date1
print(out.days)

# find the date after 30 days

future_date = date2 + timedelta(days=30)
print(future_date)



past_date = date2 - timedelta(hours=33)
print(past_date)


# write a program to find the employees who joined after 2021-03-11

data = [
    {
        "name": "kiran",
        'joining_date': date(year=2022, month=2, day=10)
    },
{
        "name": "kiran1",
        'joining_date': date(year=2021, month=2, day=10)
    },
{
        "name": "kiran2",
        'joining_date': date(year=2022, month=3, day=20)
    }
]

def filter_employees_by_joining_date(jdate):
    for emp in data:
        joining_date = emp['joining_date']
        if joining_date > jdate:
            print(emp)


jdate = date(year=2021, month=3, day=10)

filter_employees_by_joining_date(jdate)




# display current date and time

today = datetime.now()
print(type(today))
# print only date
print(today.date())

# print time
print(today.time())


# date formating

# formating object
# we formated the python datetime
# formating and converting python datetime to string
print("*******************************")
today_date = datetime.today()
print(today_date)

my_formated_date = today_date.strftime("%d/%B/%Y %H:%M:%S")
print(my_formated_date)


# parsing string datetime into python datetime
data_str = '2021-August-27 19:09'
# need to compare with other date?
other_date_str = "2021-08-26 19:09"
# which is older date?
date_1 = datetime.strptime(data_str, "%Y-%B-%d %H:%M")
print(type(date_1))

date_2 = datetime.strptime(other_date_str, "%Y-%m-%d %H:%M")
print(type(date_2))

d = datetime(1984, 1, 10, 23, 30)
print(d.strftime("%B %d, %Y"))
# 'January 10, 1984'

print(d.strftime("%Y/%m/%d"))
# '1984/01/10'

print(d.strftime("%d %b %y"))
# '10 Jan 84'



# deal with time zone


print("--------TIME zone aware dates")
#$  pip install pytz
import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
print(utc_now)
# converting into another timezone
pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
print(pst_now)
#india_time = utc_now.astimezone(pytz.timezone("Asia/Kolkata"))
#print(india_time)

d.strftime("%Y-%m-%d %H:%M:%S")
# '1984-01-10 23:30:00'





