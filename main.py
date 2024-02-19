class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0

    def enrollStudents(self, num_students):
        self.total_strength += num_students

    def dropStudents(self, num_students):
        self.total_strength -= num_students
        # Ensure total strength is non-negative
        self.total_strength = max(0, self.total_strength)

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return "StudentsInMLOps"