class Faculty:
    def __init__(self):
        self.first_name='first name'
        self.last_name='last name'
        self.email_id='email_id'
        self.address='address'
        self.ph_no='ph.no'
        self.doj='doj'
        self.salary='salary'

    def display(self):
        print('       FACULTY DETAILS        ')
        
        print('\nFull name =',self.first_name+self.last_name)
        print('Email id  =',self.email_id)
        print('Address   =',self.address)
        print('Ph.no     =',self.ph_no)
        print('Doj       =',self.doj)
        print('Salary    =',self.salary)

faculty=Faculty()

faculty.first_name='Raj'
faculty.last_name='koushik'
faculty.email_id='koushikraj768@gmail.com'
faculty.address='13-3-51/1,salivahana nagar,vaddavalli,sattenapalli'
faculty.ph_no=8688356376
faculty.doj='13-mar-2026'
faculty.salary=3000000

faculty.display()





class Student:
    def __init__(self):
        self.first_name='first name'
        self.last_name='last name'
        self.email_id='email_id'
        self.address='address'
        self.ph_no='ph.no'
        self.doj='doj'
        self.gpa='gpa'

    def display(self):
        print('\n       STUDENT DETAILS        ')
        
        print('\nFull name =',self.first_name+self.last_name)
        print('Email id  =',self.email_id)
        print('Address   =',self.address)
        print('Ph.no     =',self.ph_no)
        print('Doj       =',self.doj)
        print('Salary    =',self.gpa)

student=Student()

student.first_name='Savaral'
student.last_name='pramodini'
student.email_id='pramodini123@gmail.com'
student.address='13-3-51/1,salivahana nagar,vaddavalli,sattenapalli'
student.ph_no=8688356376
student.doj='13-mar-2026'
student.gpa=9.5

student.display()

