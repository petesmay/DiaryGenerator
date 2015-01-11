'''
Created on 8 Jan 2014

@author: pete
'''

import datetime

DAY = datetime.timedelta(1)

def generate_diary(year):
    """ Generate a weekday diary, separating each week by "-"s """
    f = "Diary-"+str(year)+".txt"
    print f
    diary = open(f, 'w+')
    
    # get the first day of the year
    date = datetime.date(year, 1, 1)
    if date.weekday()>=5:
        # saturday or sunday, find the next monday
        date.replace(year, 1, (8-date.weekday()))
    
    while date.year == year:
        write_week(date, diary)
        days = datetime.timedelta((7-date.weekday()))
        date = date+days
        
    diary.close()        
    
def write_week(start_date, diary):
    """ Write the date followed by day of the week for the weekdays"""
    while start_date.weekday()<5:
        diary.write(start_date.strftime("%y-%m-%d %A:"))
        diary.write('\n\n')
        start_date = start_date+DAY
    diary.write("-"*20)
    diary.write('\n\n')


if __name__ == '__main__':
    import sys
    if len(sys.argv)!=2:
        print "Run as "+sys.argv[0]+" <year>"
    else:
        generate_diary(int(sys.argv[1]))