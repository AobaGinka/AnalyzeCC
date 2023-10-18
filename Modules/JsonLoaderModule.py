import json
import os

class JsonLoader:
    def __init__(self, path: str) -> None:
        with open(path, "r") as f:
            self.data = json.load(f)
    
class CloneJsonLoader(JsonLoader):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def getLanguage(self) -> str:
        return self.data["environment"]["clone_detector"]["parameters"]["language"]
    
    def getThreshold(self) -> int:
        return int(self.data["environment"]["clone_detector"]["parameters"]["threshold"])
    
    def getClonePairs(self) -> list:
        return self.data["clone_pairs"]
    
    def getFileTable(self) -> list:
        return self.data["file_table"]
    

class GarbageMethodsJsonLoader(JsonLoader):
    def __init__(self, path: str) -> None:
        self.available = True
        if path == None:
            self.available = False
            return
        super().__init__(path)

    def getGarbageMethods(self) -> list:
        return self.data["methods"]
    
    def getAvailable(self) -> bool:
        return self.available