class Task:
    startTime = 0
    endTime = 0
    goalTime = 0
    taskName = ""

    def __init__(self, tn, st, gt):
        self.taskName = tn
        self.startTime = st
        self.goalTime = gt

    def setEndTime(self, et):
        self.endTime = et

