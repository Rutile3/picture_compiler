# picture_compiler

Windows環境を前提に記述します。

## 仮想環境の構築＆起動

仮想環境の作成

``` powershell
python -m venv venv
```

仮想環境の起動

``` powershell
.\venv\Scripts\activate
```

セキュリティポリシーに引っかかる場合

``` powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process    
```

仮想環境の停止

``` powershell
deactivate
```

## 単体テスト

``` powershell
\picture_compiler> pytest tests
```

## exe化

``` powershell
pyinstaller .\main.py --clean --onefile --name=picture_compiler.exe
```

``` powershell
pyinstaller main.spec --onefile
```
