# I declare that my work contains no examples of misconduct, such as plagiarism, or 
#collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: ………w1953276……………..… 
 
# Date: …12/13/2022…………………..… 

#assigning variables
progress=0
progress_module_trailer=0
exclude=0
do_not_progress_module_retriever=0
outcome=0
#creting empty lists
list1=[]
list2=[]
list3=[]
list4=[]
#creating dictionary
idlist1={}

def outcome(scorelist,progression_outcome):
      a=0
      #extending list
      scorelist.extend([pass_credits,defer_credits,fail_credits])
      print(progression_outcome)
      while a<len(scorelist):
          y=str(scorelist[a:a+3])
          y=y.replace("[","")
          y=y.replace("]","")
          #updating list
          idlist1.update({i_d+":":progression_outcome +" - "+y})
          a=a+3        
      return
def marks(status,mylist,status_count):
    a=0  
    for i in range(1,status_count+1):
       print(status,end="")
       y=str(mylist[a:a+3])
       y=y.replace("[","")
       y=y.replace("]","")
       print(y)
       #writing to  file
       f.write(status)
       f.write(str(y))
       f.write("\n")  
       a=a+3

while True:
    i_d=input("Enter your id: ")
    if i_d[0]=='w' and len(i_d)==8:  #condition for a valid id

      break
    else:
      print("invalid")
      continue   

while True:

 while True:
     try:#try and except for pass_Credits
       pass_credits=int(input("Please enter your credits at pass: "))
       while pass_credits%20!=0 or pass_credits>120:
           print("Out of range")
           pass_credits=int(input("Please enter your credits at pass: "))
       break
        
     except ValueError:
         print("Integer required")
         
 while True:
     try:#try and except for defer_Credits
       defer_credits=int(input("Please enter your credits at defer: "))   
       while defer_credits%20!=0 or defer_credits>120:
           print("Out of range")
           defer_credits=int(input("Please enter your credits at defer: "))
       break
     except ValueError:
       print("Integer required")
 while True:
     
     try:#try and except for fail_credits
       fail_credits=int(input("please enter your credits at fail: "))
       while fail_credits%20!=0 or fail_credits>120:
           print("Out of range")
           fail_credits=int(input("please enter your credits at fail: "))
       break
     except ValueError:
       print("Integer required")
  #getting total     
 total=pass_credits+defer_credits+fail_credits
 
 while total!= 120:
      print("Total incorrect")
      total==0
      pass_credits=int(input("Please enter your credits at pass: "))
      defer_credits=int(input("Please enter your credits at defer: "))
      fail_credits=int(input("please enter your credits at fail: ")) 
      total=pass_credits+defer_credits+fail_credits
     
 else:
      total=pass_credits+defer_credits+fail_credits
    
 if pass_credits==120 and defer_credits==0 and fail_credits==0 and total==120:
       #calling outcome funtion for progress
     outcome(list1,"progress")
     progress+=1                     
      
 elif pass_credits==100 and total==120:
       #calling outcome funtion for progress(module trailer)
     outcome(list2,"progress(module trailer)")
     progress_module_trailer+=1
      
 elif fail_credits>=80 and total==120:
       #calling outcome funtion for Exclude
     outcome(list3,"Exclude")    
     exclude+=1
      
 elif total==120:
       #calling outcome funtion for Do not progress – module retriever
     outcome( list4,"Do not progress – module retriever")
     do_not_progress_module_retriever+=1
            
 print("")
 x=input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')

 while x!="y" and x!="q":#condition for invalid entry
     print("Invalid enter again")
     print("")
     x= input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')
     print("")
 
 else:
       if x=="y":
        
        while True:
            i_d=input("Enter your id: ")
           
            if  i_d[0]=='w' and len(i_d)==8:
                break
            
            else:
              print("invalid")
              
       elif x=='q':
         False

         break
    
print("Histogram")
print("")
outcome=progress+progress_module_trailer+exclude+do_not_progress_module_retriever
#printing histogram
print("Progress",progress,":","*"*progress)
print("Trailer",progress_module_trailer,":","*"*progress_module_trailer)
print("Retriever",do_not_progress_module_retriever,":","*"*do_not_progress_module_retriever)
print("Exclude",exclude,":","*"*exclude)
print("")
print(outcome,"outcomes in total")
print("")	
#opening file for writing
f = open("student_mark.txt", "w")

if progress>0:
#calling marks funtion for progress
  marks("progress = ",list1,progress)
 #calling marks funtion for progress(module trailer)
if progress_module_trailer>0:
     marks("progress(module trailer) = ",list2,progress_module_trailer)
#calling marks funtion for Do not progress – module retriever
if do_not_progress_module_retriever>0:   
    marks("Do not progress – module retriever = ",list4,do_not_progress_module_retriever          )
if exclude>0:
     marks("Exclude = ",list3,exclude)

print("")
print("Marks stored in student_mark.text")
#opening file for read
f=open("student_mark.txt","r")
print(f.read())

#printing dictionary
for i in idlist1.items():    
    print(*i)
#closing file
    
f.close()


