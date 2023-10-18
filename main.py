import sys
import os

from Modules.JsonLoaderModule import CloneJsonLoader
from Modules.JsonLoaderModule import GarbageMethodsJsonLoader
from Modules.AnalyzerModule import Analyzer
from Modules.MarkdownGeneratorModule import MarkdownGenerator

OUTPUT_PATH = "./out/output.md"
GARBAGE_METHODS_PATH = "./Resources/garvage-methods.json"

def main(path: str, garbage_path: str):
    loader = CloneJsonLoader(path)
    garbage = GarbageMethodsJsonLoader(garbage_path)
    analyzer = Analyzer(loader, garbage)
    generator = MarkdownGenerator(analyzer)

    with open(OUTPUT_PATH, "w") as file:
        file.write(generator.generateReport())
    
if __name__ == "__main__":
    args = sys.argv
    # コマンドライン引数が適切な数あるかどうか
    if len(args) < 2:
        print("[Error] Arguments are too short.")
        exit()
    if len(args) == 2:
        garbage_path = None
    else:
        garbage_path = args[2]
    # 第二引数のチェック
    # 指定された場所が存在しているか
    if not os.path.exists(args[1]):
        print("[Error] It is a place that doesn't exist.")
        exit()
    # ファイルかどうか
    if not os.path.isfile(args[1]):
        print("[Error] This file is not exist.")
        exit()
    # main関数呼び出し
    main(args[1], garbage_path)