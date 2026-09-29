# #multiple inheri
# class hospital:
#     def display_hospital(self):
#         pass
# class department:
#     def __init__(self):
#     def display_department(self):
#         pass
#     def display_department(self):
#         pass
# class patient(hospital,department):
#     def __init__(self):
#         hospital.__init__(self)
#         department.__init__(self)
#
#     def full_summary(self):
#         hospital.display_hospital(self)
#         department.display_department(self)
#     def set_discharge(self):
        class Hospital:
            def __init__(self):
                self.hos_name = input("Enter Hospital Name:")
                self.location = input("Enter Location:")
                self.phone = input("Enter Phone:")

            def display_hospital(self):
                print(self.hos_name, self.location, self.phone)

        class Department:
            def __init__(self):
                self.dept_name = input("Enter Department Name:")
                self.doctor_name = input("Enter Doctor Name:")

            def display_department(self):
                print(self.dept_name, self.doctor_name)

        class Patient(Hospital, Department):
            def __init__(self):
                Hospital.__init__(self)
                Department.__init__(self)

                self.patient_name = input("Enter Patient Name:")
                self.age = int(input("Enter Age:"))
                self.gender = input("Enter Gender:")
                self.admission_date = input("Enter Admission Date:")
                self.bedno = input("Enter Bed Number:")
                self.discharge_date = input("Enter Discharge Date:")

            def set_discharge(self):
                self.discharge_date = input("Enter Discharge Date:")
                print("Discharge Date Updated:", self.discharge_date)

            def full_summary(self):
                print("\n--- Hospital Details ---")
                super().display_hospital()

                print("\n--- Department Details ---")
                self.display_department()

                print("\n--- Patient Details ---")
                print(self.patient_name)
                print(self.age)
                print(self.gender)
                print(self.admission_date)
                print(self.bedno)
                print(self.discharge_date)

        p = Patient()
        p.full_summary()
        p.set_discharge()