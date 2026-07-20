list=[2,3,4]
list.append(5)
t=(2,3,4)
t.pop()

class solution1:
    def creature1(self):
        print("creature 1")
class solution2(solution1):
    def creature2(self):
        print("creature 2")
    def creature3(self):
        print("creature 3")

sol=solution2()
sol.creature1()