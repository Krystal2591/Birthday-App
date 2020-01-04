import datetime


print ("--------------------BIRTHDAY APP----------------")


def get_birthday():
    year=int(input("What year were you born?"))
    month=int(input("What month were you born?"))
    day=int(input("What day were you born?"))
    bday=datetime.date(year, month, day)
    return bday

def date_difference(b_day,today):
    adjusted_b_day=datetime.date(today.year, b_day.month, b_day.day)
    diff=adjusted_b_day-today
    return diff.days

def display_info(diff):
    if diff>0:
        print("Your bday is in {} days!".format(diff))
    elif diff<0:
        print("Your bday was {} days ago".format(-diff))
    else:
        print("Your bday is today!")








def print_info():
    user_input=get_birthday()
    today=datetime.date.today()
    days=date_difference(user_input, today)
    display_info(days)







print_info()



