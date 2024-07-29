from pathlib import Path
import json
from datetime import datetime


class JsonExtractor:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def readJson(self):
        if not self.file_path.exists():
            return "File not found"
        try:
            with self.file_path.open('r') as file:
                data_dict = json.load(file)
                return data_dict
        except (json.JSONDecodeError, ValueError) as e:
            return "Bad input"

    def insertToDic(self, value, data):
        next_key = f"value{len(data) + 1}"
        data[next_key] = value

    def saveDatatoJsonFile(self, dataDic):
        file = Path('extracted_json.json')
        with file.open('w') as jsonFile:
            json.dump(dataDic, jsonFile, indent=4)

    def dateConversion(self,value):
        dateFormat = "%Y/%m/%d %H:%M:%S"
        datetime.strptime(value, dateFormat)
        date = datetime.strptime(value, dateFormat)
        updatedDate = date.replace(year=2021)
        return updatedDate.strftime(dateFormat)

    def strConversion(self,value):
        newValue = value.replace(" ", "")
        return newValue[::-1]

    def listConversion(self,value):
        newList = []
        for element in value:
            if not element in newList:
                newList.append(element)
        return newList

    def dataExtractor(self):
        data = self.readJson()
        if isinstance(data, str):
            return data
        extractedData = {}
        for value in data.values():
            if isinstance(value, str):
                try:
                    updatedDateStr = self.dateConversion(value)
                    self.insertToDic(updatedDateStr, extractedData)
                    continue
                except ValueError:
                    reversedValue = self.strConversion(value)
                    self.insertToDic(reversedValue, extractedData)
                    continue
            elif isinstance(value, list):
                newList = self.listConversion(value)
                self.insertToDic(newList, extractedData)
        self.saveDatatoJsonFile(extractedData)

