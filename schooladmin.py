# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 20:38:11 2021

@author: Roshni Tasya
"""

import csv


def write_into_csv(info_list):
    with open ('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])
            
            writer.writerow(info_list)
        
if __name__=='__main__':
    condition = True 
    student_num = 1 

    
    while(condition):
        student_info = input("Enter information of student #{} in the following format (name age contact no email id) :". format(student_num))
        student_info_list = student_info.split(' ') 
    
    print("\nThe entered information is -\n Name: {}\n Age : {} \n Contact No: {} \n Email ID: {}".
          format(student_info_list[0],student_info_list[1], student_info_list[2], student_info_list[3]))
    
    
    choice_check = input("Is The entered information correct? yes/no :")
   
    if choice_check == "yes":
        write_into_csv(student_info_list)
        
        condition_check = input("Do you want to enter the information of another student (yes/no) :")
        if condition_check=="yes":
            student_num = student_num+1
        elif condition_check=="no":
                condition = False 
                
                
                
    elif choice_check=="no":
        print("\n Please re enter")
            
       