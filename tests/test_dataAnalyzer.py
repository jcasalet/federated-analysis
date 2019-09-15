import unittest
from app.dataAnalyzer import FederatedDataAnalyzer

class TestDataAnalyzer(unittest.TestCase):

    def test_readConfigFile(self):
        fieldFilter = [{'fieldName': 'ER', 'fieldType': 'categorical', 'fieldValues': ['Positive', 'Negative', 'NA']}, \
                       {'fieldName': 'PgR', 'fieldType': 'categorical', 'fieldValues': ['Positive', 'Negative', 'NA']}, \
                       {'fieldName': 'HER2', 'fieldType': 'categorical', 'fieldValues': ['0', '1+', '2+', '3+', 'NA']}, \
                       {'fieldName': 'Age at onset', 'fieldType': 'numerical', 'fieldValues': []}, \
                       {'fieldName': 'Tissue type (3 groups)', 'fieldType': 'free-form', 'fieldValues': ['ascii', 'utf-8']}]

        configFileName = 'tests/test_conf.json'
        myFederatedDataAnalyzer = FederatedDataAnalyzer(configFileName)
        with self.subTest():
            self.assertEqual(myFederatedDataAnalyzer.configFile.fileName, 'tests/test_data.csv', 'wrong data file')
        with self.subTest():
            self.assertEqual(myFederatedDataAnalyzer.configFile.fileHeader, 'True', 'wrong file header')
        with self.subTest():
            self.assertEqual(myFederatedDataAnalyzer.configFile.fieldDelimiter, ',', 'wrong field delimiter')
        with self.subTest():
            self.assertEqual(myFederatedDataAnalyzer.configFile.fieldFilter, fieldFilter, 'wrong field filter')

'''
    def test_readDataFile():

        # test me

    def test_validateField():

        # test me

    def test_getStatistics():

        # test me

    def test_run():

        # test me
'''