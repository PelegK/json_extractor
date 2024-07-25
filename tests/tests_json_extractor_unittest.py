import unittest
from pathlib import Path
import json
from json_extractor import JsonExtractor

class TestJsonExtractor(unittest.TestCase):

    def setUp(self):
        self.valid_file = Path("data/python_exercise.json")
        self.test_file = Path("tests/test_data.json")
        self.corrupt_file = Path("tests/corrupt.json")
        self.no_file = Path("no_file.json")
        self.output_file = Path("extracted_json.json")
    
    def test01_fileNotFound(self):
        extractor = JsonExtractor(self.no_file)
        result = extractor.readJson()
        self.assertEqual(result, "File not found")

    def test02_badInput(self):
        extractor = JsonExtractor(self.corrupt_file)
        result = extractor.readJson()
        self.assertEqual(result, "Bad input")

    def test03_fileRead(self):
        extractor = JsonExtractor(self.test_file)
        data = extractor.readJson()
        expectedData = {
        "value1": ["boy","boy","girl","girl","boygirl"],
        "value2": "tel aviv",
        "value3": "2007-03-10 00:00:00",
        "value4": "2008/01/28 00:00:00"
        }
        self.assertEqual(data, expectedData)
    
    def test04_dataInsertion(self):
        extractor = JsonExtractor(self.no_file)
        myDict = {"value1":"xyz", "value2":"abc"}
        newValue = "abcde"
        extractor.insertToDic(newValue,myDict)
        expectedDict =  {"value1":"xyz", "value2":"abc", "value3":"abcde"}
        self.assertEqual(len(myDict), 3)
        self.assertEqual(myDict, expectedDict)

    def test05_extractorFileNotFound(self):
        extractor = JsonExtractor(self.no_file)
        result = extractor.dataExtractor()
        self.assertEqual(result, "File not found")

    def test06_extractorBadInput(self):
        extractor = JsonExtractor(self.corrupt_file)
        result = extractor.dataExtractor()
        self.assertEqual(result, "Bad input")

    def test07_extractorSuccess(self):
        extractor = JsonExtractor(self.test_file)
        extractor.dataExtractor()
        with self.output_file.open('r') as file:
            result = json.load(file)
        expectedData = {
        "value1": ["boy","girl","boygirl"],
        "value2": "vivalet",
        "value3": "00:00:0001-30-7002",
        "value4": "2021/01/28 00:00:00"
        }
        self.assertEqual(result, expectedData)

