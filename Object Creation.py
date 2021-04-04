class Car_Wheel:
    total_wheels = 0 
    def __new__(self, value):
        # new method is called first for object creation
        if Car_Wheel.total_wheels < 5:
            Car_Wheel.total_wheels += 1
            return super().__new__(self)
        else:
            raise Exception('Only five car wheels are allowed!!')

    def __init__(self, side):
        # Initiliazer is called for initializing values
        self.side = side
        print(f"{self.side} created")


if __name__ == '__main__':
    wheel_01 = Car_Wheel('Front Left')
    wheel_02 = Car_Wheel('Front Right')
    wheel_03 = Car_Wheel('Rear Left')
    wheel_04 = Car_Wheel('Rear Right')
    wheel_05 = Car_Wheel('Puncture wheel')

    try:
        print('Trying creating extra wheel')
        wheel_06 = Car_Wheel('No side')
    except Exception as msg:
        print(msg)



