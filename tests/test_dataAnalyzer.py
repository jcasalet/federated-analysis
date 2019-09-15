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
            assert myFederatedDataAnalyzer.configFile.fileName == 'tests/test_data.csv'
        with self.subTest():
            assert myFederatedDataAnalyzer.configFile.fileHeader == 'True'
        with self.subTest():
            assert myFederatedDataAnalyzer.configFile.fieldDelimiter == ','
        with self.subTest():
            assert myFederatedDataAnalyzer.configFile.fieldFilter == fieldFilter


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