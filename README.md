# 概要
[CCFinder-SW](https://github.com/YuichiSemura/CCFinderSW)で出力されるJSONファイルから、コードクローン群を分析するプログラムです.
# 使い方
- Python3.11.5における実行のみテストを行いました.
  - `python main.py <clone-json> <garbage-json>`
- `./out/output.md`に出力されます.
## 引数
### 必須
- \<clone-json>にはCCFinder-SWで出力されたJSONファイルのパスを指定する.
### Option
- \<garbage-json>には[GarbageMethodsSearcher](https://github.com/AobaGinka/GarbageMethodsSearcher)で出力されたJSONファイルのパスを指定する.