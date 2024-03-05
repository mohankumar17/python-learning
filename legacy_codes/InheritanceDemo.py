class ParentA:
    def __init__(self):
        print("ParentA Constructor")
    def showMsgA(self):
        print("ParentA")

class ParentB:
    def __init__(self):
        print("ParentB Constructor")
    def showMsgB(self):
        print("ParentB")
class ChildA(ParentA, ParentB):
    def __init__(self):
        super().__init__()
        print("ChildA Constructor")
    def healthCheck(self):
        return True
    def showMsgA(self):
        print("ChildA: showMsgA override")
    def showMsgB(self):
        print("ChildB: showMsgA override")

chOb = ChildA()
chOb.showMsgA()
chOb.showMsgB()
