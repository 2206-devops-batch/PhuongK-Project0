class patients:
    # patient info is entered by an admin after patient fills out paperwork.
    total_num_patients = 0

    def __init__(self, fn, ln, birthday, gender, number, address):
        self.fn = fn
        self.ln = ln
        self.birthday = birthday
        self.gender = gender
        self.number = number
        self.address = address
        patients.total_num_patients += 1
        with open('list_patients.txt', 'a+') as file:
            file.write('\n' + fn + ' ' + ln + ' ' + birthday + ' ' + gender + ' ' + number + ' ' + address)

    def get_info(self):
        print(self.fn, self.ln, self.birthday, self.gender)
        
    def get_contact(self):
        print(self.number, self.address)

    def get_ins(self, company='None', id='None'):
        # if patient is cash patient, 
        self.company = company
        self.id = id

    def patient_records(self, date):
        pass


# patient check in and checkout
# patient conditions/treatment/medications
# patient appointments


