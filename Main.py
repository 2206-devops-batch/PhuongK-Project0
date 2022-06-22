from employee import doctors as D
from employee import nurses as N
from patient import patients as P
import string

atoz = string.ascii_lowercase

def main():
    userinput = (input('Enter p for new patient, d for new doctor or n for a new nurse: '))
    if (userinput) == 'p':
        person = 'patient\'s'
    elif (userinput) == 'd':
        person = 'doctor\'s'
    elif (userinput) == 'n':
        person = 'nurse\'s'
    else:
        raise ValueError('Please enter p, d or n')

    userfn = input(f"Please enter the {person} first name: ")
    userln = input(f"Please enter the {person} last name: ")
    userbirthday = input(f"Please enter the {person} birthday in the format MM/DD/YYYY: ")
    if len(userbirthday) != 10:
        raise TypeError('Please enter a valid birthday in the proper format')
    elif userbirthday in atoz:
        raise TypeError('Please enter a valid birthday in the proper format')
    elif int(userbirthday[:2]) <= 0 or int(userbirthday[:2]) > 12:
        raise ValueError('Please enter a valid birthday in the proper format')
    elif int(userbirthday[3:5]) <= 0 or int(userbirthday[:2]) > 31:
        raise ValueError('Please enter a valid birthday in the proper format')
    elif int(userbirthday[6:]) > 2022:
        raise ValueError('Please enter a valid birthday in the proper format')
    elif userbirthday[2] != '/' or userbirthday[5] != '/':
        raise ValueError('Please enter a valid birthday in the proper format')

    usergender = input(f"Please enter the {person} gender, 'Male', 'Female' or 'Non-binary': ")
    if usergender != 'Male' and usergender != 'Female' and usergender != 'Non-binary':
        raise ValueError('Please choose a valid option')

    usernumber = input(f"Please enter the {person} number in the format 123-456-7890: ")
    if len(usernumber) != 12:
        raise TypeError('Please enter a valid birthday in the proper format')
    elif usernumber in atoz:
        raise TypeError('Please enter a valid number in the proper format')
    elif usernumber[3] != '-' or usernumber[7] != '-':
        raise ValueError('Please enter a valid number in the proper format')

    useraddress = input(f"Please enter the {person} address.\n")

    if userinput == 'p':
        new_patient = P(userfn, userln, userbirthday, usergender, usernumber, useraddress)
        print('The patient list has been updated!')
    elif userinput == 'd':
        new_doctor = D(userfn, userln, userbirthday, usergender, usernumber, useraddress)
        print(f'{userfn} {userln} has been added to the list of doctors!')
    elif userinput == 'n':
        new_nurse = N(userfn, userln, userbirthday, usergender, usernumber, useraddress)
        print(f'{userfn} {userln} has been added to the list of nurses!')
    

main()

# Future Functionalities
# Admin Login
# Pull patient/doctor/nurse info
# Edit info
# patient appointments
# patient treatment
# patient medical records
# different departments
