import datetime

# declare a dictionary and make it a global variable
user_pass_dict={} # empty dictionary that will store the username and passwords
with open("user.txt", "r") as f:
    for user_file in f: # use a for loop to iterate through the file, line by line and store in dictionary
        new_line_strip = user_file.strip("\n") # strip the new line character in the file
        # perform a split which will also turn the content of file into a list, and break the file into 
        # 2 seperate strings 'username' and 'password' that can now be stored into the dictionary
        user_file_split = new_line_strip.split(",") 
        username= user_file_split[0]
        password= user_file_split[1]
        user_pass_dict[username.lower()] = password # username is the key and password is the value in dictionary

# ====code for user to login=====

login = False   # create a flage for the infinite while loop
while not login:    # create a while loop to help iterate through the steps
                    # until the user enters the correct username and password
    with open("user.txt", "r+") as f:  # open the file 'user.txt in read/write mode'
        user_name_password = input("enter user name: ") + "," + " " + input("enter password: ")
        
        # use the for loop to iterate through the login file to check if username and password is valid
        for linereading in f:
            login_file_strip = linereading.strip("\n") # strip the new line character

            # if stament to compare the user input with file records
            if user_name_password == login_file_strip:
                print("login sucessful")
                login = True
                break   # exit the loop if correct username and password was entered

        if not login:   # if username and password is wrong display message
            print(" invalid username or password enter again")


# define function for admin user to register other users

def reg_user_function():
    with open("user.txt", "a") as f:
        print("Add a new user to record: ")
        username = input("enter username:").lower()
        while username.lower() in user_pass_dict:
            print("username already existing choose another username")
            username = input("enter username again:").lower()
        print("user name accepted")
        
        print("please enter password: ")
        password = input("enter password: ")
        print(" please confirm password")
        confirm_password = input("enter password confirmation: ")
            # use a while loop to iterate through the password input process
            # password and password confirmation input matches
        while password != confirm_password:
            print("password does not match")
            confirm_password = input("please enter password again: ")
        print("password saved succesfully")
        username_password = username + "," + " " + password
        f.write("\n"+ username_password) # write the new username and password to file
#test_reg_admin = reg_user_function()


# add_task function — that is called when a user selects ‘ a ’ to add a new task.
def add_task_function():
    with open("tasks.txt", "a") as f: # open file task.txt in append mode
        # declare all variables to store the values to be written to file task.txt
        
        x = datetime.datetime.now()  # current date and tine
        # date when task was assigned
        date_now_assign = (x.strftime("%d"),x.strftime("%b"),x.strftime("%Y"))
        date_now_assign =([str(n) for n in date_now_assign]) # convert to string
        date_now_assign= (' '.join(date_now_assign)) 
        
        # due date of task
        # this variable will help collect the date input from user in user friendly format
        due_date_input = datetime.date( int(input("enter year for due date: ")),\
            int(input("enter month in number format e.g april =04: ")),\
            int(input("enter date: ")))
        y = due_date_input
        due_date = (y.strftime("%d"),y.strftime("%b"),y.strftime("%Y"))
        # convert to string
        due_date = [str(n) for n in due_date]
        due_date = (' '.join(due_date)) # due date for task submission
        # save all inputs into a variable to be written to the task.txt file
        task_user = input("enter username: ") + "," + " " + input("enter the title of the task: ")\
            + "," + " " + input("enter description of task: ") + "," + " " +\
            date_now_assign + "," +" " + due_date + "," + " " + "No"
        f.write("\n" + task_user)   # write values to file
#test_task_add = add_task_function()


# view_all function — that is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’.
def view_all_function():
    with open("tasks.txt", "r") as f:   # open file in read mode
        # perform split on file content and store into individual variable 
        # for easy refrence and readabilty
        for task_file_all in f:
            username_va,title_va,task_va,assgn_date_va,date_due_va,completed_va = task_file_all.split(", ")
            print(f"""
                Name : {username_va}
                Task Title: {title_va}
                Task description: {task_va}
                Date assigned : {assgn_date_va}
                Task due date: {date_due_va}
                Is task Completed : {completed_va}
                """)
#view_all_function()

# view_mine function — that is called when users type ‘vm’ to view all the tasks that have been assigned to them.
def view_mine_function():
    with open("tasks.txt", "r") as f:   # open file in read mode
        user = user_name_password.split(', ')   
    
        # create an empty list to store the list of task. this will make it easy to count the number of task
        all_task_list = []
        task_num = 0 # declare a variable to count the task and initialise to 0 
        # perform split on file content and store into individual variable 
        # for easy refrence and readabilty
        for task_file in f:# read  line in file and store to variable
            task_file = task_file.strip('\n')
            username,task_title,task_desc,assgn_date,date_due,completed = task_file.split(", ")
            
            all_task_list.append(task_file.split(", "))
            task_num += 1
            
            
            if user[0] == username:
                print(f"""
                task number: {task_num}
                Name : {username}
                Task Title: {task_title}
                Task description: {task_desc}
                Date assigned : {assgn_date}
                Task due date: {date_due}
                Is task Completed : {completed}
                """)
 
        while True: # while loop to continously bring up the menu
        
            print("select a task by entering the corresponding number to the task:")
            select_task_num = int(input("select the task number: ")) # variable to select task num
            print("select any of the letters in menu to edit task")
            print(f'''
                tc   :   mark task complete
                ed   :   edit task
                -1   :   Exit to edit menu
                
            ''')
            task = all_task_list[select_task_num]  # the task line in the file
            task_menu = input("enter task menu key to edit 'tc' or 'ed' or em to exit: ")
            
            if task_menu == "tc" and task[-1].lower() == "no":
                task[-1] = input("type in 'Yes' to mark task as complete: ")                                
                all_task_list[select_task_num] = task
                
            elif task[-1].lower() != "no" and task_menu == "tc"  :
                print("Task already completed")

            # if user select 'ed' to edit task
            

            elif task_menu == "ed": 
                print(f'''
                eu   :   edit user
                edt  :   edit due date
                ex   :   exit menu
                ''')
               
                while True: # while loop to continuosly loop through the sub menu
                    
                    edit_task_menu = input("enter 'eu' or edt or 'ex' to exit: ")
                    if edit_task_menu == "eu":
                        task[0] = input("enter name of user: ")                
                        all_task_list[select_task_num] = task

                    elif edit_task_menu=="edt":
                        task[4] = datetime.date( int(input("enter year for due date: ")),\
                                    int(input("enter month in number format e.g april =04: ")),\
                                    int(input("enter date: ")))
                        y = task[4]
                        task[4] = (y.strftime("%d"),y.strftime("%b"),y.strftime("%Y"))
                        # convert to string
                        task[4] = [str(n) for n in task[4]]
                        task[4] = (' '.join(task[4])) # due date for task submission                
                        all_task_list[select_task_num] = task
                    elif edit_task_menu=="ex":
                        break # exit the submenu loop

            elif task_menu == "-1":
                break # exit to main menu
    # block of codes to commit and write all changes to file
        all_task_join = ''
        for t in all_task_list:
            all_task_join += ', '.join(t) + '\n'
        #all_task_strip = all_task_join.strip("\n")
        #print(all_task_join)
        #print(f"{all_task_join}")
        #f.write(task_join)
        with open("tasks.txt", "w") as f:
            all_task_join = all_task_join.strip('\n')
            f.writelines(all_task_join)
                                
#view_mine_function()


# defunction function to generate task_overview report

with open("tasks.txt", "r") as f:
    # read the lines in file tasks.txt and store in variable
    tasks = f.readlines()
    # check the total lines in files since there is one task per line, 
    # this will give us the total number of task 
    total_task = len(tasks)

# number of completed tasks

def task_overview_function():
    with open("tasks.txt", "r") as f:
        count = 0 # count the number of completed task
        no_count = 0 # count the number of uncompleted task
        overdue_count = 0 # count overdue task
    
        for task_file in f:# read  line in file and store to variable
            task_file = task_file.strip('\n') # strip the new line character
            username,task_title,task_desc,assgn_date,date_due,task_status = task_file.split(", ")
            # convert date stored in file from string to date for date comparing.
            date_due_conv = datetime.datetime.strptime(date_due, '%d %b %Y')
            assgn_date_conv = datetime.datetime.strptime(assgn_date, '%d %b %Y')
            # every completed task is set to yes, use the if statement to check the task that has 'yes'
            # and count them into variable count 
            if task_status.lower() == 'yes': 
                count = count +1
            #  number of uncompleted tasks and percentage of uncompleted task
            elif task_status.lower() == 'no': 
                no_count = no_count +1
                # percentage of uncompleted task
                no_count_percent = (no_count/total_task)*100 

            # compare dates using if statment
            if date_due_conv.date() < assgn_date_conv.date() and task_status.lower() == "no":
                overdue_count = overdue_count +1
                # percentage of task that are overdue
                count_overdue_percent =(overdue_count/total_task)*100
                #count_overdue_percent =(count_overdue/total_task)*100            

    return f"""total number of task is : {total_task}\nTotal Number of completed task: {count}\
    \nTotal Number of uncompleted task: {no_count}\nTotal Number of overdue task: {overdue_count}\
    \nTotal percentage of uncompleted task: {no_count_percent}%\
    \nTotal percentage of overdue task: {count_overdue_percent}%
    """

    # open task_overview.txt(not existing yet) file write mode and write the results to file
with open("task_overview.txt", "w") as f:
    # call the task overview function
    f.write(task_overview_function())

#task_overview = task_overview_function()

# open task_overview.txt(not existing yet) file write mode and write the results to file

with open("task_overview.txt", "w") as f:
    # call the task overview function
    f.write(task_overview_function())


# === define function to display user_overview.txt===

with open("user.txt", "r") as f:
    # read the lines in file user.txt and store in variable
    admin_login = f.readlines()
    # check the total lines in files since there is one user per line, 
    # this will give us the total number of users 
    total_users = len(admin_login)

# The total number of tasks assigned to that user.
# define a function to carry out this task
   
def eachuser(userna, nut):    
    count_task_user = 0
    percentage_total_task = 0
    count_assign_task_completed = 0
    count_assign_task_uncompleted = 0
    percentage_assign_task_uncompleted = 0
    percentage_assign_task_completed = 0
    overdue_count = 0
    count_overdue_percent = 0
    with open("tasks.txt", "r") as f:
        #count = 0 # count the number of task assigned to user
        for task_file in f:# read  line in file and store to variable
            task_file = task_file.strip('\n') # strip the new line character
            username,task_title,task_desc,assgn_date,date_due,task_status = task_file.split(", ")
            # convert date stored in file from string to date for date comparing.
            date_due_conv = datetime.datetime.strptime(date_due, '%d %b %Y')
            assgn_date_conv = datetime.datetime.strptime(assgn_date, '%d %b %Y')
            if username == userna:
                count_task_user += 1
                if task_status.lower() == "yes":
                    count_assign_task_completed +=1
            
                elif task_status.lower() == "no":
                    count_assign_task_uncompleted += 1
            # compare dates using if statment
            if date_due_conv.date() < assgn_date_conv.date() and task_status.lower() == "no":
                overdue_count = overdue_count +1
                
                             

        # code block for calculating task percentages
        if count_task_user > 0:
            percentage_assign_task_completed = (count_assign_task_completed/count_task_user)*100
            percentage_assign_task_uncompleted = (count_assign_task_uncompleted/count_task_user)*100
        if total_task > 0:
            percentage_total_task = (count_task_user/total_task) * 100
            count_overdue_percent =(overdue_count/total_task)*100 # percentage of task that are overdue
        

    return f"""Tasks for user: {userna}
The total number of task for user is {count_task_user}\n\
The total percentage of task assigned {percentage_total_task}%\n\
The total percentage of assigned task completed {percentage_assign_task_completed}%\n\
The total percentage of assigned task uncompleted {percentage_assign_task_uncompleted}%\n\
The total percentage of task uncompleted and overdue{percentage_assign_task_uncompleted}%
"""


# while loop to return to Menu options
while True:

    user = user_name_password.split(', ')  
    # if username and password is correct then print the below:
    if user[0] == "admin":
        print(f"""
            Please select one of the folowing options:
            a  -   add task
            va -   view all task
            vm -   view my task
            r   -   Register new user
            gr  -   Generate report
            ds  -   Display statistics
            e   -   exit
            """)
    else:
        print(
            "Please select one of the folowing options:\n"
            "a  -   add task\n"
            "va -   view all task\n"
            "vm -   view my task\n"
            "e  -   exit"
        )

    # ==== If the user chooses ‘r’ to register, write another user name and password to file =====

    # declare variable that will store the user choice from menu
    user_option = input("please enter option from menu: ")
    # declare if statement for when user chooses menu option 'r'
    if user_option == "r" and user[0] == 'admin':
        reg_user_function() # call function to register user


    #=======If the user chooses ‘a’ to add a task==========
    elif user_option == "a":
        add_task_function() # call function to add task
        
    # ======If the user chooses ‘va’ display the information for all task in the file # on the screen =======
    elif user_option == "va":
        view_all_function() # call function to view all task

# ===If the user chooses ‘vm’ display the information for the user that is logged on  # on the screen ====#
    elif user_option == "vm":
        view_mine_function()

# === if user chooses 'gr' generate user over view and task overview report files====
    elif user_option == "gr" and user[0] == 'admin':
        # call the function to write to file user_overview.txt
        usertask = '' # number of tasks per user
        for user in user_pass_dict.keys():
            usertask += eachuser(user, total_task)
        with open("user_overview.txt","w") as f:
            f.write(f"Total number of task is : {total_task}\nThe total number of users registered is :{ total_users}")
            f.write('\n'+usertask)
        # call function to write to file the task_overview.txt
        with open("task_overview.txt", "w") as f:
            # call the task overview function
            f.write(task_overview_function())
    

#===== display statistic ========

# == if user chooses 'ds' display user view and task overview report files
    elif user_option == "ds" and user[0] == 'admin':
        print("This is the task over view report:\n"+ task_overview_function())
        print(f"This is the user overview report:\n{usertask}")

    

    # menu option 'e' Exit 
    elif user_option == "e":
        break