from field_name_phone_birthday import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, number:str):
         self.phones.append(Phone(number))
    
    def remove_phone(self, number:str):
         self.phones = list(filter(lambda phone: phone == number, self.phones))

    def edit_phone(self, old_number, new_number):
            if self.find_phone(old_number):  
                self.phones = list(map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones
              ))
            else:
                raise ValueError(f'Phone {old_number} not found!')
         
    def find_phone(self, number:str):
        for phone in self.phones:
              if phone.value == number:
                   return phone
              
    def add_birthday(self, date):
         self.birthday = Birthday(date)
              
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"