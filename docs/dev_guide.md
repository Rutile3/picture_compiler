
# 開発ガイド

## 📗 概要

この文書は「picture_compiler」の開発ガイドです。

## 📝 単体テスト

仮想環境を起動し、以下のコマンドを実行してください。

``` powershell
\picture_compiler> pytest tests # 単体テストの実行
```

## 💾 exe化

仮想環境を起動し、以下のコマンドを実行してください。

``` powershell
pyinstaller .\main.py --clean --onefile --name=picture_compiler.exe #
```
