class A:
    def feature1(self):
        print("I am a feature1")
    def feature2(self):
        print("I am a feature2")
class B:
    def feature3(self):
        print("I am a feature3")
    def feature4(self):
        print("I am a feature4")
class C(A,B):
    def feature5(self):
        print("I am a feature5")

c=C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()