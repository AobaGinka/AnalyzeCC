from Modules.AnalyzerModule import Analyzer

class MarkdownGenerator:
    def __init__(self, analyzer:Analyzer) -> None:
        self.analyzer = analyzer

    def generateReport(self):
        report = ""
        report += self.generateInfo()
        report += self.generateFileCountReport()
        report += self.generateClonesReport()
        return report
        
    def generateInfo(self):
        text = """
# 基本情報
- **言語**: {}
- **しきい値**: {}
- **クローンの数**: {}
""".format(self.analyzer.getLanguage(), str(self.analyzer.getThresHold()), str(self.analyzer.getNumberOfClones()))
        return text
    
    def generateFileCountReport(self):
        text = "# ファイルごとの関連クローンの数\n"
        file_count = self.analyzer.getFileCount()
        for key1 in file_count.keys():
            text += "## {}\n".format(key1)
            for key2 in file_count[key1].keys():
                if file_count[key1][key2] > 0:
                    text += key2 + ": " + str(file_count[key1][key2]) + "\n"
        return text

    def generateClonesReport(self):
        text = "# クローン一覧\n"
        clone_pairs = self.analyzer.getClonesList()
        file_table = self.analyzer.getFileTable()
        file_list = self.analyzer.getFileList()
        n = 1
        for pair in clone_pairs:
            fragment1_fileid = int(pair["fragment1"]["file_id"])
            fragment2_fileid = int(pair["fragment2"]["file_id"])
            text += "## ClonePair{}\n".format(n)
            text += "### " + file_table[fragment1_fileid]["path"] + "\n"
            text += "```\n"
            for s in file_list[fragment1_fileid][pair["fragment1"]["begin"]-1:pair["fragment1"]["end"]-1]:
                text += s + "\n"
            text += "```\n"
            text += "### " + file_table[fragment2_fileid]["path"] + "\n"
            text += "```\n"
            for s in file_list[fragment2_fileid][pair["fragment2"]["begin"]-1:pair["fragment2"]["end"]-1]:
                text += s + "\n"
            text += "```\n"
            n += 1
        return text