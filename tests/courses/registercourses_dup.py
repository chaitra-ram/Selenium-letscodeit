from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import pytest, unittest
from ddt import data, unpack, ddt

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetup):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "10", "1220", "10"), ("Learn Python 3 from scratch", "20", "1220", "20"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccName, ccExp, ccCVV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.driver.find_element_by_link_text("All Courses").click()