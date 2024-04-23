from random import randint
import winsound
from csv import writer
import datetime
import mysql.connector as sqlconn
import matplotlib.pyplot as pl
import pandas as pd

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
def beep():
    f=600
    d=200
    winsound.Beep(f,d)
def beep1():
    f=800
    d=800
    winsound.Beep(f,d)
def append_list_as_row(file_name, list_of_elem):

    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
def times():
    D=datetime.datetime.now()
    d=str(D)
    d=d[:10]
    return d
def commaspacing(a):
    fs=1
    ss=1
    ts=4    
    if len(a) == 4:
         return print(a[0:fs],',',a[ss:ts],sep='')
    
    elif len(a) == 5:
         return  print(a[0:fs+1],',',a[ss+1:ts+2],sep='')
        
    elif len(a) == 6:
         return print(a[0:1],',',a[1:fs+2],',',a[ss+2:ts+4],sep='')
     
    elif len(a) == 7:
         return print(a[0:2],',',a[2:fs+3],',',a[ss+3:ts+6],sep='')
def menu():
    print('\n\n-------------------------------')
    print("| 1. | Deposit                |")
    print('-------------------------------')
    print("| 2. | Withdrawal             |")
    print('-------------------------------')
    print("| 3. | Balance                |")
    print('-------------------------------')
    print("| 4. | Modify Account Details |")
    print('-------------------------------')
    print("| 5. | Exit                   |")
    print('-------------------------------')
def menu1():
    print("\n\nWhat Details Would You Like to Update ?")
    print('\n\n-------------------------------')
    print("| 1. | Name                   |")
    print('-------------------------------')
    print("| 2. | Regno                  |")
    print('-------------------------------')
    print("| 3. | Pin                    |")
    print('-------------------------------')
    print("| 4. | Account Type           |")
    print('-------------------------------')
    print("| 5. | Address                |")
    print('-------------------------------')
    print("| 6. | Spouse\'s Name          |")
    print('-------------------------------')
    print("| 7. | Father\'s Phone Number  |")
    print('-------------------------------')
    print("| 8. | Go Back                |")
    print('-------------------------------')