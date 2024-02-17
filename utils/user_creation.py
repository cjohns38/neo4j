from faker import Faker

fake = Faker()


class Create_Person:
    def __init__(self):
        self.uuid = fake.uuid4()
        self.fname = fake.first_name()
        self.lname = fake.last_name()
        self.username = fake.user_name()
        self.is_vip = fake.boolean(chance_of_getting_true=.01)
        self.dob = fake.date_of_birth(minimum_age=21, maximum_age=90)
        self.ssn = fake.ssn()
        self.phone = fake.phone_number()

        self.address = fake.street_address()
        self.post_code = fake.postcode()
        self.crs = fake.pydecimal(min_value=0, max_value=1, right_digits=2)

    def describe(self):
        print(f'UUID: {self.uuid}')
        print(f'First name: {self.fname}')
        print(f'Last name: {self.lname}')
        print(f'Username: {self.username}')
        print(f'is_vip: {self.is_vip}')
        print(f'DOB: {self.dob}')
        print(f'SSN: {self.ssn}')
        print(f'Phone: {self.phone}')
        print(f'Address: {self.address}')
        print(f'Post Code: {self.post_code}')
        print(f'CRS: {self.crs}')

    def cypfer_query(self):
        params = {"uuid": self.uuid,
                  "fname": self.fname,
                  "lname": self.lname,
                  "username": self.username,
                  "is_vip": self.is_vip,
                  "dob": self.dob,
                  "ssn": self.ssn,
                  "phone": self.phone,
                  "address": self.address,
                  "post_code": self.post_code,
                  # 'crs': self.crs
                  }
        return params