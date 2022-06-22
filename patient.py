# Hospital or clinic patient management system
# - GOAL: check in patients, get them to appropriate place of treament, checkout in orderly fashion and to facilitate
# patients receiving appropriate medical care
# - Departments: Reception, Radiology, Anesthetics, OR (surgery), ER, Burn Center, ICU, Maternity Ward, Occupational Therapy
# - Medical Records, Pharmacy,

# - Modules #
# Staff Menu - doctors, nurses etc
# Patient Menu
# Appointment Menu
# Room List 
# Medical Records Menu

# CHECKIN #
# Patient fills out sign-in sheet, hospital associates input data into system, system outputs appropriate department
# to transfer patient to based on sign-in sheet, also sends to Doctor(s) or Nurse(s) to review and ok it.

# Patient Care #
# - Room Availability
# - Patient care status - Waiting (w), Triage (t), Doctor(d), finished (F) and waiting to be discharged

# CHECKOUT, DISCHARGE # 
# Documentation recorded on the patient and their treatment, conditions, etc are saved 
# Patient receives discharge notes and prescriptions, referrals, follow-up appointments etc if needed

class patients:
    # patient info is entered by an admin after patient fills out paperwork.
    # 
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


