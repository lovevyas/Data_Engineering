from abc import ABC, abstractclassmethod

class Employee(ABC):
    def __init__(self, id, name, email):
        self.id = id
        self._name = name
        self._email = email
    def details(self):
        print("ID:",self._id,"\n")
        print("Name",self._name,"\n")
        print("Email",self._email,"\n")
    def check_base_pay(self):
        pass
    def check_bonus(self):
        pass
    @abstractclassmethod
    def calculateSalary():
        pass

class RegularEmployee(Employee):
    __salary = 0
    def __init__(self,id, name, email,base_pay,bonus=0):
        self._id = id
        self._name = name
        self._email = email
        self.__base_pay = base_pay
        self.bonus = bonus
        if(self.bonus>0):
            self.__salary = base_pay + bonus
        else:
            self.__salary =  base_pay
        self.details()
    def change_email(self,email):
        self._email = email
    
    def salary_change(self,changed_base_pay):
        self.__base_pay = self.changed_base_pay
    
    def check_base_pay(self):
        return self.__base_pay
    def check_bonus(self):
        return self.bonus
    def calculateSalary(self):
        return self.__base_pay

class Manager(Employee):
    _salary = 0
    def __init__(self,id, name, email,base_pay,bonus=0):
        self._id = id
        self._name = name
        self._email = email
        self.__base_pay = base_pay
        if(bonus>0):
            self._bonus = bonus
        else:
            self._bonus = base_pay*(0.2)        
        self.__salary = self.__base_pay+self._bonus
        self.details()

    def change_email(self,email):
        self._email = email
    
    def salary_change(self,changed_base_pay):
        self.__base_pay = self.check_base_pay
    

    def check_base_pay(self):
        return self.__base_pay
    def check_bonus(self):
        return self._bonus
    
    def calculateSalary(self):
        return int(self.__salary)

class Contractor(Employee):
    _salary = 0
    def __init__(self,id, name, email,hourly_rate,bonus=0):
        self._id = id
        self._name = name
        self._email = email
        self.__base_pay = hourly_rate
        self.details()
        self._bonus=bonus

    def change_email(self,email):
        self._email = email
    
    def salary_change(self,changed_base_pay):
        self.__base_pay = self.check_base_pay
    
    
    def check_base_pay(self):
        return self.__base_pay
    def check_bonus(self):
        return self._bonus

    def calculateSalary(self, hours_worked):
        self.__salary = self.__base_pay*hours_worked
        self.__salary+= self._bonus
        return self.__salary


Leo = RegularEmployee(101,"Leo","vyas@gmail",10000)
Leo.details()


Rohan  = Manager(201,"Rohan","rohan@gmail",5000)
Mahin = Contractor(301,"Mahin","mahin@gmail.com",1000)

a = Leo.calculateSalary()
b = Rohan.calculateSalary()
c = Mahin.calculateSalary(10)
print(a,b,c)

employee = {
    Manager(201,"Suraj","rohan@gmail",5000),
    Contractor(301,"Amy","mahin@gmail.com",1000),
    RegularEmployee(101,"Love","vyas@gmail",10000)
}

karan = Manager(901,"karan","karan@gmail.com",1000,4000)

print(karan.check_bonus())
print(karan.calculateSalary())


