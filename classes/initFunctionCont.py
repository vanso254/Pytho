class User:
    def __init__(self,username,gender,email,phone):
        self.username=username
        self.gender=gender
        self.email=email
        self.phone=phone
        
person1=User("John Doe","Male","johndoe@email.com","+2547000000")

print(person1.username,person1.email)