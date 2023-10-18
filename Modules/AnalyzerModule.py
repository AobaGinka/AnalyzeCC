from Modules.JsonLoaderModule import CloneJsonLoader
from Modules.JsonLoaderModule import GarbageMethodsJsonLoader

class Analyzer:
    def __init__(self, loader: CloneJsonLoader, garbage: GarbageMethodsJsonLoader) -> None:
        self.loader = loader
        self.garbage = garbage
        # ファイルリスト
        self.file_list = []
        self.loadFileList()
        # クローンリスト
        self.clone_pairs = self.loader.getClonePairs()
        if self.loader.getLanguage() == "java":
            self.classifyClonesOfJava()
        # ファイルカウント
        self.file_count = {}
        self.countFile()

    def loadFileList(self):
        # ファイルの中身をまとめたリスト
        # 順番はidに対応
        for file_data in self.loader.getFileTable():
            with open(file_data["path"], "r") as f:
                self.file_list.append(f.read().splitlines())

    def classifyClonesOfJava(self):
        # import文の除去
        self.removeImport()
        # getter/setterの除去
        if self.garbage.getAvailable():
            self.removeGetterSetter()
            
    def removeImport(self):
        for pair in self.clone_pairs[:]:
            fragment1_fileid = int(pair["fragment1"]["file_id"])
            for s in self.file_list[fragment1_fileid][pair["fragment1"]["begin"]-1:pair["fragment1"]["end"]-1]:
                if "import" in s:
                    self.clone_pairs.remove(pair)
                    break

    def removeGetterSetter(self):
        garbage_methods = self.garbage.getGarbageMethods()
        for pair in self.clone_pairs[:]:
            clone1_begin = pair["fragment1"]["begin"]
            clone1_end = pair["fragment1"]["end"]
            for garbage in garbage_methods:
                if pair["fragment1"]["file_id"] == garbage["file_id"]:
                    if clone1_begin <= garbage["begin"] and garbage["begin"] <= clone1_end:
                        self.clone_pairs.remove(pair)
                        break
                    if clone1_end <= garbage["end"] and garbage["end"] <= clone1_end:
                        self.clone_pairs.remove(pair)
                        break
    
    def countFile(self):
        file_table = self.loader.getFileTable()
        # dictの初期化
        for i in file_table:
            self.file_count[i["path"]] = {}
            for j in file_table:
                self.file_count[i["path"]][j["path"]] = 0
        # カウント
        for pair in self.clone_pairs:
            self.file_count[file_table[pair["fragment1"]["file_id"]]["path"]][file_table[pair["fragment2"]["file_id"]]["path"]] += 1
    
    def getFileList(self) -> list:
        return self.file_list
    
    def getClonesList(self) -> list:
        return self.clone_pairs
    
    def getFileCount(self) -> dict:
        return self.file_count

    def getLanguage(self) -> str:
        return self.loader.getLanguage()
    
    def getThresHold(self) -> int:
        return self.loader.getThreshold()
    
    def getNumberOfClones(self) -> int:
        return len(self.clone_pairs)
    
    def getFileTable(self) -> list:
        return self.loader.getFileTable()