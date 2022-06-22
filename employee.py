class employees:
    def __init__(self, fn, ln, birthday, gender, number, address):
        self.fn = fn
        self.ln = ln
        self.birthday = birthday
        self.gender = gender
        self.number = number
        self.address = address

class doctors(employees):
    total_num_doctors = 0
    def __init__(self, fn, ln, birthday, gender, number, address):
        doctors.total_num_doctors += 1
        with open('list_doctors.txt', 'a+') as file:
            file.write('\n' + fn + ' ' + ln + ' ' + birthday + ' ' + gender + ' ' + number + ' ' + address)

    def get_info(self):
        print(self.fn, self.ln, self.birthday, self.gender)
        
    def get_contact(self):
        print(self.number, self.address)

# doctor availablility
# doctor specialty

class nurses(employees):
    total_num_nurses = 0
    def __init__(self, fn, ln, birthday, gender, number, address):
        nurses.total_num_nurses += 1
        with open('list_nurses.txt', 'a+') as file:
            file.write('\n' + fn + ' ' + ln + ' ' + birthday + ' ' + gender + ' ' + number + ' ' + address)

    def get_info(self):
        print(self.fn, self.ln, self.birthday, self.gender)
        
    def get_contact(self):
        print(self.number, self.address)

# nurse specialty
# nurse availability
