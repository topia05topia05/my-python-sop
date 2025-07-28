# チュートリアル Step 2: 最初のサイト公開

## 目的

このステップの目的は、我々の知的資産（ドキュメント）を、**世界中の誰もがアクセスできる、ウェブサイト**として、**自動で**、公開する、究極のワークフローを、構築することです。

**前提：** Step 1の、全ての、手順が、完了していること。

---

## 手順

### 1. 武器の導入（MkDocsのインストール）

聖域の中に、サイトを構築するための道具を、導入します。

1.  `(.venv)` が有効化されたターミナルで、以下のコマンドを実行してください。
    ```bash
    pip install mkdocs mkdocs-material
    ```

### 2. サイトの骨格生成

`mkdocs`に、サイトの基本構造を、自動で、作らせます。

1.  ターミナルで、以下のコマンドを実行してください。（最後のドット`.`を忘れずに）
    ```bash
    mkdocs new .
    ```
    これにより、`docs`フォルダと`mkdocs.yml`ファイルが、生成されます。

### 3. Git & GitHubとの連携

ローカルのプロジェクトを、クラウド上のGitHubと接続し、自動化の準備をします。

1.  **Gitの初期化と、最初のコミット:**
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```
2.  **GitHub上で、新しい、空のリポジトリを作成します。**
3.  GitHubの指示に従い、ローカルリポジトリを、リモートに接続し、最初の`push`を、行なってください。
    ```bash
    git remote add origin <GitHubリポジトリのURL>
    git branch -M main
    git push -u origin main
    ```

### 4. 自動化の契約（GitHub Actionsの設定）

`git push`するだけで、サイトが自動で更新される、魔法の契約書を作成します。

1.  プロジェクトのルートに、`.github/workflows/ci.yml` という、ファイルを作成します。
2.  このファイルに、**[リファレンス：GitHub Actions設定](/reference/ci_yml/)** に書かれている、最新の、ワークフロー設定を、コピー＆ペーストしてください。
3.  変更を、コミットし、GitHubに、プッシュします。
    ```bash
    git add .
    git commit -m "Add GitHub Actions workflow"
    git push
    ```

### 5. 権限と、公開の、最終設定

GitHubに、ロボットの権限と、サイトの公開元を、教えます。

1.  GitHubリポジトリの `Settings` > `Actions` > `General` で、**`Workflow permissions`** を **`Read and write permissions`** に設定します。
2.  `Settings` > `Pages` で、**`Branch`** を **`gh-pages`** に設定し、`Save`します。

### 6. 勝利の確認

数分後、`Settings` > `Pages` のページをリロードすると、あなたのサイトが、公開されたURLが表示されます。

---

おめでとうございます。
あなたは、ただ、ドキュメントを書くだけでなく、その、知的資産を、世界に向けて、自動で、発信し続ける、強力な、パイプラインを、その手に、入れました。