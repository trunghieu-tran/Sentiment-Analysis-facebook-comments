from unittest import TestCase
from Main2 import analysis_text

class testRunAnalys(TestCase):
    def test1(self):
        self.assertEqual(1, 1)

class testsetResult(TestCase):
    def test_setAll(self):
        myanalysis = analysis_text()
        myanalysis.__init__()
        myanalysis.setResult("neg", 0.5)
        myanalysis.setResult("pos", 0.2)
        myanalysis.setResult("neu", 0.3)

        self.assertEqual(myanalysis.negativeLabel.cget("text"), "Отрицательно : 0.5 % \n")
        self.assertEqual(myanalysis.positiveLabel.cget("text"), "Положительно : 0.2 % \n")
        self.assertEqual(myanalysis.neutralLabel.cget("text"), "Нейтрально : 0.3 % \n")

    def test_setAll_0(self):
        myanalysis = analysis_text()
        myanalysis.__init__()
        myanalysis.setResult("neg", 0)
        myanalysis.setResult("pos", 0)
        myanalysis.setResult("neu", 0)

        self.assertEqual(myanalysis.negativeLabel.cget("text"), "Отрицательно : 0 % \n")
        self.assertEqual(myanalysis.positiveLabel.cget("text"), "Положительно : 0 % \n")
        self.assertEqual(myanalysis.neutralLabel.cget("text"), "Нейтрально : 0 % \n")

    def test_setOne(self):
        myanalysis = analysis_text()
        myanalysis.__init__()
        myanalysis.setResult("neg", 0.1)

        self.assertEqual(myanalysis.negativeLabel.cget("text"), "Отрицательно : 0.1 % \n")
        self.assertEqual(myanalysis.positiveLabel.cget("text"), "")
        self.assertEqual(myanalysis.neutralLabel.cget("text"), "")

    def test_NUL(self):
        myanalysis = analysis_text()
        myanalysis.__init__()

        self.assertEqual(myanalysis.negativeLabel.cget("text"), "")
        self.assertEqual(myanalysis.positiveLabel.cget("text"), "")
        self.assertEqual(myanalysis.neutralLabel.cget("text"), "")

    def test_setErrorType(self):
        myanalysis = analysis_text()
        myanalysis.__init__()
        myanalysis.setResult("error", 0.1)

        self.assertEqual(myanalysis.negativeLabel.cget("text"), "")
        self.assertEqual(myanalysis.positiveLabel.cget("text"), "")
        self.assertEqual(myanalysis.neutralLabel.cget("text"), "")

    def test_setErrorValue(self):
        myanalysis = analysis_text()
        myanalysis.__init__()
        myanalysis.setResult("pos", "abc")
        self.assertEqual(myanalysis.negativeLabel.cget("text"), "")
        self.assertEqual(myanalysis.positiveLabel.cget("text"), "")
        self.assertEqual(myanalysis.neutralLabel.cget("text"), "")