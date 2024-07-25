import sys
import pytest
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import json
from json_extractor import JsonExtractor

def test01_fileNotFound():
    noFile = Path ('noFile.json')
    extractor = JsonExtractor(noFile)
    result = extractor.readJson()
    assert result == "File not found"

def test02_badInput():
    corruptFile = Path("tests/corrupt.json")
    extractor = JsonExtractor(corruptFile)
    result = extractor.readJson()
    assert result == "Bad input"

def test03_fileRead():
    file = Path("tests/test_data.json")
    extractor = JsonExtractor(file)
    data = extractor.readJson()
    expectedData = {
    "value1": ["boy","boy","girl","girl","boygirl"],
    "value2": "tel aviv",
    "value3": "2007-03-10 00:00:00",
    "value4": "2008/01/28 00:00:00"
    }
    assert data == expectedData

def test04_dataInsertion():
    file = Path("path")
    myDict = {"value1":"xyz", "value2":"abc"}
    newValue = "abcde"
    extractor = JsonExtractor(file)
    extractor.insertToDic(newValue,myDict)
    expectedDict =  {"value1":"xyz", "value2":"abc", "value3":"abcde"}
    assert len(myDict) == 3
    assert myDict == expectedDict

def test05_saveJsonFile():
    file = Path("path")
    outputFile = Path("extracted_json.json")
    myDict = {"myDict": "1234"}
    extractor = JsonExtractor(file)
    extractor.saveDatatoJsonFile(myDict)
    with outputFile.open('r') as file:
        result = json.load(file)
    expectedData = {"myDict": "1234"}
    assert result == expectedData

def test06_extractorBadInput():
    file = Path("tests/corrupt.json")
    extractor = JsonExtractor(file)
    result = extractor.dataExtractor()
    assert result == "Bad input"

def test07_extractorFileNotFound():
    file = Path("noFile.json")
    extractor = JsonExtractor(file)
    result = extractor.dataExtractor()
    assert result == "File not found"

def test08_extractorSuccess():
    file = Path("tests/test_data.json")
    outputFile = Path("extracted_json.json")
    extractor = JsonExtractor(file)
    extractor.dataExtractor()
    with outputFile.open('r') as file:
        results = json.load(file)
    expectedData = {
        "value1": ["boy","girl","boygirl"],
        "value2": "vivalet",
        "value3": "00:00:0001-30-7002",
        "value4": "2021/01/28 00:00:00"
    }
    assert results == expectedData

