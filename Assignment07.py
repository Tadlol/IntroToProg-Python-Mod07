# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# TTharp,5.18.2023,Modified code functions to complete assignment 06
# TTharp,5.19.2023,Tested code, cleared errors, commented code.
# TTharp,5.31.2023 Added error handling and used pickle to change to .dat file
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
import pickle

# Declare variables and constants
file_name_str = "ToDoFile.dat"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    @staticmethod
    def read_data_from_file(file_obj, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param: file_obj (string) with name of file
        :param: list_of_rows: (list) you want filled with file data
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try:
            with open(file_obj, "rb") as file:
                list_of_rows.extend(pickle.load(file))
        except FileNotFoundError:
            with open(file_obj, "wb"):
                pass
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: list_of_rows (list) of dictionary rows
        """

        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        table_lst.append(row)
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :return: table_lst (list) of dictionary rows
        """
        for list_of_rows in table_lst:
           if list_of_rows["Task"].lower() == task.lower():
              table_lst.remove(list_of_rows)
        else:
            print(task + " is not on the list, please try again.\n")
        return table_lst

    @staticmethod
    def write_data_to_file(file_obj):
        with open(file_obj, "wb") as file:
            pickle.dump(table_lst, file)
        return table_lst



# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: choice (string)
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        print("******* The current tasks ToDo are: *******")
        if not list_of_rows:
            print("No tasks found.")
        else:
            for row in list_of_rows:
                print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :param: task (string) task title
        :param: priority (string) task priority
        :return: task, priority (string, string) with task and priority
        """
        task = input("Enter a new task: ")
        priority = input("Enter " + task + "'s priority:")

        return task, priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :param: task (string) task to remove
        :return: task (string) with task
        """
        task = input("What task would you like to remove? ")

        return task

    @staticmethod
    def save_state():
        """  Confirms save state of the list fom the user

        :return: state (string) save state of list
        """

        save_state = input("Did you save the list already? (y/n): ")

        return save_state

    @staticmethod
    def error_msg():
        """  print error message to the user

        :return: nothing
        """
        print("You entered an unaccepted value, please try again.\n")

# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_obj=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_obj=file_name_str)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        state = IO.save_state()  # Confirms Save state
        if state.lower() == "n":
            table_lst = Processor.write_data_to_file(file_obj=file_name_str)  # Saves data
            print("Data saved, Goodbye!")
            break  # Exits program by exiting loop
        elif state.lower() == "y":
            print("Goodbye!")
            break  # Exits program by exiting loop
        else:
            IO.error_msg()
            continue
    else:
        IO.error_msg()
        continue
