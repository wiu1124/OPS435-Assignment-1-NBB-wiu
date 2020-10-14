#! /usr/bin/env python3

'''
OPS435 Assignment 1 - Fall 2020
Program: a1_wiu.py
Author: Wesley Iu
Date: 10/12/2020

The python code in this file (a1_wiu.py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description: This program will convert date formats in YYYY-MM-DD, YYYY/MM/DD or YYYY.MM.DD to regular the regular date format (i.e October 24th, 2020).
'''

import os
import sys

def usage():
    print('Usage: a1_wiu.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD')
    return

def sanitize(obj1, obj2):
    obj1 = user_raw_data.replace('/', '').replace('.', '').replace('-','')
    obj2 = allow_chars.replace(user_raw_data, '')
    return obj1

def size_check(obj, intobj):
    obj = dob
    intobj = 8
    if len(obj) != 8:
     return False
    
def range_check(obj1, obj2):
    obj1 = year
    obj2 = range(1900,10000)
    if int(obj1) in obj2:
     return True
    else:
     return False
    return obj1

def leap_year(obj3):
    if (int(obj3) % 4) == 0:
     if (int(obj3) % 100) == 0:
       if (int(obj3) % 400) ==0:
        return True
       else:
        return False
     else:
      return True
    else:
     return False

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      usage()
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # step 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
      result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)

        
