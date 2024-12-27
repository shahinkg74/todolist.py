
class Task:
    def __init__(self, task_id, title, state=False, date_of_finishing=None):
        self.task_id = task_id
        self.title = title
        self.state = state 
        self.date_of_finishing = date_of_finishing 

    def done(self):
        self.state = True

    def undone(self):
        self.state = False

    def __str__(self):
        status = "Completed" if self.state else "Pending"
        date_str = self.date_of_finishing.strftime("%Y-%m-%d") if self.date_of_finishing else "Not set"
        return f"Task ID: {self.task_id}, Title: '{self.title}', Status: {status}, Expected Completion: {date_str}"
