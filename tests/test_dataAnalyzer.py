import unittest
from app.dataAnalyzer import FederatedDataAnalyzer

class TestDataAnalyzer(unittest.TestCase):


    def test_readConfigFile(self):
        configFileName = 'tests/test_conf.json'
        myFDA = FederatedDataAnalyzer(configFileName)
        fieldFilter = [{'fieldName': 'ER', 'fieldType': 'categorical', 'fieldValues': ['Positive', 'Negative', 'NA']}, \
                       {'fieldName': 'PgR', 'fieldType': 'categorical', 'fieldValues': ['Positive', 'Negative', 'NA']}, \
                       {'fieldName': 'HER2', 'fieldType': 'categorical', 'fieldValues': ['0', '1+', '2+', '3+', 'NA']}, \
                       {'fieldName': 'Age at onset', 'fieldType': 'numerical', 'fieldValues': []}, \
                       {'fieldName': 'Tissue type (3 groups)', 'fieldType': 'free-form', 'fieldValues': ['ascii']}]
        with self.subTest():
            self.assertEqual(myFDA.configFile.fileName, 'tests/test_data.csv', 'wrong data file')
        with self.subTest():
            self.assertEqual(myFDA.configFile.fileHeader, 'True', 'wrong file header')
        with self.subTest():
            self.assertEqual(myFDA.configFile.fieldDelimiter, ',', 'wrong field delimiter')
        with self.subTest():
            self.assertEqual(myFDA.configFile.fieldFilter, fieldFilter, 'wrong field filter')


    def test_readDataFile(self):
        configFileName = 'tests/test_conf.json'
        myFDA = FederatedDataAnalyzer(configFileName)
        with self.subTest():
            self.assertEqual(myFDA.dataFile.iloc[2]['HER2'], '2+', 'wrong field value')
        with self.subTest():
            self.assertEqual(myFDA.dataFile.iloc[1]['PgR'], 'Negative', 'wrong field value')
        with self.subTest():
            self.assertEqual(myFDA.dataFile.iloc[0]['ER'], 'Positive', 'wrong field value')

    def test_validateField(self):
        configFileName = 'tests/test_conf.json'
        myFDA = FederatedDataAnalyzer(configFileName)
        # test categorical for categorical
        with self.subTest():
            self.assertTrue(myFDA.validateField('Positive', myFDA.fieldFilter['ER']))
        # test categorical for non-categorical
        with self.subTest():
            self.assertFalse(myFDA.validateField(42, myFDA.fieldFilter['ER']))
        # test numerical for numerical
        with self.subTest():
            self.assertTrue(myFDA.validateField(42, myFDA.fieldFilter['Age at onset']))
        # test numerical for non-numerical
        with self.subTest():
            self.assertFalse(myFDA.validateField('Positive', myFDA.fieldFilter['Age at onset']))
        # test free-form for free-form
        with self.subTest():
            self.assertTrue(myFDA.validateField('42', myFDA.fieldFilter['Tissue type (3 groups)']))
        # test free-form for non-free-form
        with self.subTest():
            self.assertFalse(myFDA.validateField("\u00ff8", myFDA.fieldFilter['Tissue type (3 groups)']))


    def test_run(self):
        configFileName = 'tests/test_conf.json'
        myFDA = FederatedDataAnalyzer(configFileName)
        self.assertTrue(myFDA.run(), msg='integration test failure')

