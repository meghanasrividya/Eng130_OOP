
import datetime


def age(birthdate) :
    # create today's object
    t= datetime.date.today()
    # py variable gives th boolean ouput 0 or 1.
    # If the birthday has passed this year then py =0 orelse it will be 1 ,which can subtracted from end result
    py = (t.month,t.day)<(birthdate.month,birthdate.day)
    #to calculate the difference in years
    num_years=t.year-birthdate.year
    age= num_years-py
    return age


year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
day= int(input("Enter a day: "))
birthdate=datetime.date(year,month,day)
print(age(birthdate))
