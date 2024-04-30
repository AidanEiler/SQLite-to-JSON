import sqlalchemy as db
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Customer():
    
    def __init__(self, id, fname, lname, dob, city, state, zip): 
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.dob = dob
        self.city = city 
        self.state = state
        self.zip = zip 
        
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def age(d):
        dob = datetime.strptime(d, '%Y-%m-%d')
        today = datetime.today()
        age = relativedelta(today, dob)
        return age.years
    
    def adult(self):
        return self.age() >= 18
    
    def to_json(self):
        j =  {}
        j.update(self.__dict__)
        j["id"] = self.id
        j["first_name"] = self.first_name
        j["last_name"] = self.last_name
        j["dob"] = self.dob
        j["city"] = self.city
        j["state"] = self.state
        j["zip"] = self.zip
        j["age"] = self.age()
        j["full_name"] = self.full_name()
        j["adult"] = self.adult()
        return j
    
engine = db.create_engine('sqlite:///../input/cutomer-sqlite/customer.sqlite') # used Kaggle to make this project
connection = engine.connect()

query = db.text('SELECT * FROM customer')
result_proxy = connection.execute(query)
connection.close()
results = result_proxy.fetchall()

#for demonstration/debugging 
#for row in results:
#    customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
#    print (customer.to_json())
