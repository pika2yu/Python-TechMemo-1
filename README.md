# Python-TechMemo-1

MacでPythonとJupyter Notebookをインストールする手順<br>
以下をターミナルで実行する。<br>
1. install the ‘brew’ package manager for mac<br>
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"<br>
2. install python, pip, and jupyter<br>
   brew tap homebrew/core<br>
   brew install python@3.10<br>
   brew install jupyter<br>
3. セットアップはこれで完了<br>
   jupyter notebook は以下で実行できる<br>
   jupyter lab
