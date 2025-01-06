from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
  
  def add_record(self, record):
    if record.name.value == self.data:
        raise KeyError(f"Record with name '{record.name.value}' already exists.")
    self.data[record.name.value] = record

  def find(self, name):
     record = self.data.get(name, None)
     if record is None:
        raise KeyError(f"Record with name '{name}' not found.")
     return record
  
  def delete(self, name):
     if name not in self.data:
        raise KeyError(f"Record with name '{name}' not found.")
     del self.data[name]

  def get_upcoming_birthdays(self):
     today_date = datetime.today().date()
     upcoming_birthdays = []

     for name, record in self.data.items():
        if record.birthday:
            birthday_date = record.birthday.value.replace( year=today_date.year).date()
            timedelta_days = (birthday_date - today_date).days
            if 0 <= timedelta_days <= 7:
               if birthday_date.weekday() > 4:
                  days_delta = 2 if birthday_date.weekday() == 5 else 1
                  congratulation_date = birthday_date + timedelta(days=days_delta)
               else:
                  congratulation_date = birthday_date
                  upcoming_birthdays.append(
                        {
                            "name": name,
                            "congratulation_date": congratulation_date.strftime(
                                "%d.%m.%Y"
                            ),
                        }
                    )
     return upcoming_birthdays