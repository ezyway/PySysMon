class Test:
    def __init__(self, one, two):
        self.one = one
        self.two = two
    
    def __del__(self):
        print("Deleted Object")

while True:
    t = Test(1,2)
    