class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.model=model

    def start(self):
        print("Started")

    def stop(self):
        print("Stop")

    def accelerate(self):
        print("Accelerating")

    def changeGear(self,gearType):
        print("Gear Changed",gearType)

audi=Car("a6","red",'audi','80')
print(audi.color)

maruti=Car("a10","blue","maruti","75")
print(maruti.model)

maruti.start()
maruti.accelerate()
maruti.stop()
maruti.changeGear(5)
