### **- The Modern Data Scientist's Blueprint -**

**凡例:**
*   `[ ]` - 未着手のタスク
*   `[✓]` - 完了済みのタスク

---

## **第1部: 我々の憲法と戦略思想 (The Constitution & Philosophy)**

### **1.1. プロジェクト憲章 (G.U.I.D.E.)**
*   **究極目標:** パートナーを、VS CodeとJupyterを自在に操る自律したマスターデータサイエンティストへと変革させる。
*   **基本思想: 『実験室と書斎』モデル**
    *   **実験室 (`notebooks/`):** 自由な試行錯誤、データとの対話、そして発見の場。
    *   **書斎 (`src/`):** 発見を、再利用可能でテストされた「知的資産」として結晶化させる場。
*   **統治原則: GitHub中心主義 (GitHub-Centric Workflow)**
    *   **唯一の情報源:** この `PLAN.md` と、GitHubリポジトリ内のIssue、コードが、全ての正義である。記憶や、このチャット上の会話に頼ることは、固く禁ずる。

---

## **第2部: プロジェクトの設計図 (The Architecture)**

### **2.1. ディレクトリ構造**
*   全てのプロジェクトは、この神聖な構造に従うこと。
    ```
    JupyterLab-project/
    ├── .venv/               # 聖域 (Python仮想環境)
    ├── data/                # 生データ置き場 (読み取り専用)
    ├── notebooks/           # 実験室 (Jupyterノートブック)
    ├── src/                 # 書斎 (再利用可能なPythonコード)
    │   └── __init__.py      # このフォルダをパッケージとして認識させる魔法
    ├── tests/               # 品質保証室 (テストコード)
    ├── .gitignore           # 無視リスト (Gitの追跡から除外するファイルを指定)
    ├── PLAN.md              # 我々の憲法 (このファイル)
    ├── README.md            # プロジェクトの顔 (概要と使い方を記述)
    └── requirements.txt     # プロジェクトの部品表 (依存ライブラリ一覧)
    ```

---

## **第3部: 戦術的ロードマップ (The Tactical Roadmap)**

### **フェーズ 0: プロジェクトの創生 (Project Genesis)**
*目的：全ての活動の基盤となる、完璧でクリーンな開発環境を定義し、創造する。*

*   `[ ]` **Task 0-1: 中央司令部の設立 (GitHub Repository)**
    1.  GitHub上に `JupyterLab-project` リポジトリを作成する。
    2.  **`Add .gitignore` ドロップダウンから `Python` を選択**し、リポジトリを初期化する。
    3.  作成したリポジトリをローカルにクローンする。

*   `[ ]` **Task 0-2: 聖域と骨格の構築 (Local Environment Setup)**
    1.  VS Codeでプロジェクトフォルダを開き、ターミナルで `python -m venv .venv` を実行して仮想環境を構築。`Select Interpreter`でそれを選択する。
    2.  上記**2.1. ディレクトリ構造**に従い、`data`, `notebooks`, `src`, `tests` ディレクトリを手で作成する。
    3.  `src` フォルダ内に、空の `__init__.py` ファイルを作成する。

*   `[ ]` **Task 0-3: 計画書の奉納と最初の記録 (Initial Commit)**
    1.  この計画書の内容で `PLAN.md` を作成・保存する。
    2.  プロジェクトの概要、目的、使い方を記述した `README.md` を作成・保存する。
    3.  `git add .` を実行し、全ての初期ファイルをステージングする。
    4.  `git commit -m "feat: Initial project structure and planning documents"` コマンドで、最初のコミットを行う。
    5.  `git push` で、我々の創造物をGitHubに奉納する。

### **フェーズ 1: 三種の神器の導入と動作確認 (Installation & Verification)**
*目的：我々の武器が、聖域内で正しく機能することを保証する。*

*   `[ ]` **Task 1-1: コアライブラリの導入**
    1.  仮想環境を有効化したターミナルで `pip install --upgrade pip` を実行。
    2.  `pip install jupyter pandas matplotlib scikit-learn` を実行。
    3.  `pip install pytest ruff black` を実行。（品質保証ツールも最初から入れるのがプロよ）
    4.  `pip freeze > requirements.txt` で、導入した全ての武器を部品表に記録する。
    5.  `git add requirements.txt` と `git commit -m "feat: Add core libraries"` で記録し、プッシュする。

*   `[ ]` **Task 1-2: 実験室の開通確認**
    1.  `notebooks/01_environment_check.ipynb` を作成。
    2.  最初のセルに `import pandas as pd; print(pd.__version__)` と書き、`Shift+Enter` で実行。バージョン番号が表示されれば、実験室は正常に機能しているわ。

### **フェーズ 2: 『実験室』でのデータとの対話 (Interactive Exploration)**
*目的：あの**成績データ**を題材に、データと対話し、その本質を理解する技術を体に刻み込む。*

*   `[ ]` **Task 2-1: データの観察と可視化**
    1.  あの `records` 辞書を `notebooks/02_grade_analysis_lab.ipynb` の最初のセルで定義する。
    2.  PandasのDataFrameに変換し、`head()`, `describe()`, `info()` でデータを多角的に観察する。
    3.  Matplotlibを使い、点数の分布を棒グラフで可視化する。

*   `[ ]` **Task 2-2: 発見の記録**
    1.  この実験ノートブックを `git add` し、`git commit -m "feat: Conduct initial grade data analysis in notebook"` でコミットし、プッシュする。

### **フェーズ 3: 『書斎』での知識の体系化 (Professional Refactoring)**
*目的：『実験室』での閃きを、再利用可能で、品質保証された『知的資産』へと昇華させる。*

*   `[ ]` **Task 3-1: コードの関数化 (Refactoring)**
    1.  `src/grade_analyzer.py` を作成する。
    2.  実験ノートブックで行った一連の分析処理（合計・平均計算、差の算出など）を、**型ヒント**と**Docstring**を完備した、一つの関数 `analyze_grades(data: dict) -> pd.DataFrame:` として清書する。

*   `[ ]]**Task 3-2: 品質保証 (Unit Testing)**
    1.  `tests/test_grade_analyzer.py` を作成する。
    2.  `pytest`を使い、`analyze_grades` 関数が、想定通りの結果を返すかを確認する、ごく簡単なテストコードを記述する。

*   `[ ]` **Task 3-3: 知的資産の活用と記録**
    1.  新しい実験ノートブック `notebooks/03_production_analysis.ipynb` を作成。
    2.  `from src.grade_analyzer import analyze_grades` で、あなたが書斎で作り上げた関数を `import` する。
    3.  その関数を使って、成績データ分析が一行で実行できることを確認する。
    4.  `git add .` し、`git commit -m "refactor: Move grade analysis logic to a function and add tests"` で、この知的な飛躍を歴史に刻み、プッシュする。

### **フェーズ 4: 究極の戦闘スタイルへ (Automation & AI)**
*目的：AIと自動化ツールを「副官」として従え、開発の速度と品質を、人間超えのレベルへと引き上げる。*

*   `[ ]` **Task 4-1: 規律の自動化 (Linter & Formatter)**
    1.  VS Codeの設定 (`settings.json`) に、`black` と `ruff` を連携させ、保存時にコードが自動で整形・チェックされるルールを記述する。

*   `[ ]` **Task 4-2: AI副官の導入 (AI Assistant)**
    1.  VS Code拡張機能 `Codeium` をインストールし、認証する。
    2.  `src/grade_analyzer.py` を開き、`# このDataFrameに合格/不合格のカラムを追加する。平均点以上を合格とする` のようなコメントを書き、AIにコードを提案させる。

*   `[ ]` **Task 4-3: 神の視点の習得 (Debugger)**
    1.  `src/grade_analyzer.py` の関数内にブレークポイントを設置。
    2.  `tests/test_grade_analyzer.py` をデバッグモードで実行 (`F5`) し、コードが途中で停止し、変数の中身を覗けることを体験する。

---

どうかしら。
これが、我々の全ての対話の歴史を尊重し、その上で、私が持つプロフェッショナルとしての知識を全て注ぎ込んだ、現時点での**究極の回答**よ。

次のステップに進む準備はいい？パートナー。