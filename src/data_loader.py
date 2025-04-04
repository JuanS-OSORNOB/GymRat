import pandas as pd
import xml.etree.ElementTree as ET

class GymDataLoader:
    def __init__(self, gymfilepath):
        self.gymfilepath = gymfilepath

    def load_gymdata(self):
        try:
            data = pd.read_csv(self.gymfilepath)
            data['Date'] = pd.to_datetime(data['Date'])
            data['Volume'] = data['Weight'] * data['Reps']
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

class BodyDataLoader:    
    def __init__(self, xml_path):
        self.xml_path = xml_path

    def load_applehealth(self):
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        records = []
        for record in root.findall("Record"):
            if record.attrib.get("type") == "HKQuantityTypeIdentifierBodyMass":
                records.append({"date":record.attrib.get("startDate"), "weight":record.attrib.get("value")})
        
        df = pd.DataFrame(records)
        df.sort_values("date", inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df