# try:
#     number = int(input("number:"))
#     print(number)
# except ValueError:
#     print("error")


# my_car.drive(30)
# name.upper()
# nemo.swim()
# my_car.add_fuel(60)


# class Arbitrary(object):
#
#     def __init__(self, data=0):
#         self.data = data
#
#     def getit(self):
#         return self.data * "!"
#
#
# class Thing(Arbitrary):
#
#     def __init__(self, value=1):
#         super().__init__(value * 2)
#
#     def getit(self):
#         return self.data * "#"
#
#
# a, b, c = Arbitrary(2), Thing(), Thing(3)
# print(a.getit(), b.getit(), c.getit())


# class SuperClass:
#     def __init__(self, x):
#         self.x = x
#
#     def __repr__(self):
#         return str(vars(self))
#
#
# class SubClass(SuperClass):
#     def __init__(self, x):
#         SuperClass.__init__(self, x)
#
#
# thing = SubClass(3)
# print(thing)

