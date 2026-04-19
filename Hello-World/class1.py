class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def drive(self):
        print("the car is driving")
car1=Car("toyota","carny")
car2=Car("honda","accord")
       
print(car1.brand)
car1.drive()

 
        