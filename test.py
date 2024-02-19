from main import StudentsInMLOps

def test_enroll_students():
    ml_ops_class = StudentsInMLOps()
    ml_ops_class.enrollStudents(5)
    assert ml_ops_class.getTotalStrength() == 5

def test_drop_students():
    ml_ops_class = StudentsInMLOps()
    ml_ops_class.enrollStudents(8)
    ml_ops_class.dropStudents(3)
    assert ml_ops_class.getTotalStrength() == 5

def test_get_class_name():
    ml_ops_class = StudentsInMLOps()
    assert ml_ops_class.getClassName() == "StudentsInMLOps"