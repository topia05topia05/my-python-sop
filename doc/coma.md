リファレンス：コマンド・チートシート
このページは、我々のワークフローで頻繁に使用する、ターミナルコマンドの、意味と、使用場面をまとめた、究極のカンニングペーパーです。

仮想環境 (venv)
コマンド	意味	使用場面
python -m venv .venv	聖域の創造: venvモジュールを使い、.venvという名前の仮想環境を、カレントディレクトリに、作成する。	各チャプターや、プロジェクトの、一番最初に、一度だけ、実行する。
.venv\Scripts\activate	聖域への入場: 仮想環境を、有効化する。	そのプロジェクトの、作業を、開始する時。
deactivate	聖域からの退場: 仮想環境を、無効化し、PCの通常環境に戻る。	そのプロジェクトの、作業を、終了する時。
pip install <lib>	武器の追加: <lib>という名前の、ライブラリを、現在の聖域にのみ、インストールする。	プロジェクトに、新しい、機能が、必要になった時。
pip freeze > reqs.txt	武器リストの記録: 現在の聖域に、インストールされている、全てのライブラリとそのバージョンを、reqs.txtというファイルに、書き出す。	他の人と、プロジェクトを、共有する前や、重要な、変更を、加えた後。
ドキュメントサイト (MkDocs)
コマンド	意味	使用場面
pip install mkdocs-material	道具の導入: mkdocs本体と、美しいmaterialテーマを、インストールする。	venvを作成した後の、一番最初に、一度だけ、実行する。
mkdocs new .	骨格の生成: docsフォルダとmkdocs.ymlを、カレントディレクトリに、自動生成する。	mkdocsを、インストールした直後に、一度だけ、実行する。
mkdocs serve	ローカルプレビュー: あなたのPCの中に、ドキュメントサイトの、プレビュー用ウェブサーバーを、立ち上げる。	.mdファイルを、編集しながら、見た目を、リアルタイムで、確認したい時。Ctrl+C`で停止。
mkdocs build	サイトの建設: docs/フォルダの内容を、静的なHTMLサイトに、変換し、site/フォルダに、出力する。（Actionsが自動でやってくれるので、我々が、手で、打つことは、もうないわ）	（自動化の裏側を、理解したい、 curiousなあなたのための、情報）
バージョン管理 (Git)
コマンド	意味	使用場面
git init	歴史の始まり: カレントディレクトリを、Gitの、バージョン管理下に、置く。	プロジェクトの、一番最初に、一度だけ、実行する。
git status	現状の確認: 「前回のセーブから、どのファイルが、変更されたか」という、現状を、表示する。	コミットする前など、常に、現状を、把握したい時に、何度でも、使う。
git add <file>	カゴに入れる: <file>という、特定のファイルを、次のセーブ（コミット）の、対象として、ステージングエリアに、追加する。（git add .で、全ての変更を、一度に、カゴに入れる）	コミットする、直前の、準備段階。
git commit -m "msg"	歴史に、刻む: カゴに入れた、全ての変更を、"msg"という、メッセージ付きで、ローカルの歴史に、記録（セーブ）する。	ファイルの、変更が、一つの、論理的な、塊として、完了した時。
git push	世界と、同期する: ローカルに記録した、新しい歴史を、クラウド上のGitHubリポジトリに、送り、内容を、一致させる。	ローカルでの、コミット作業が、一区切りついた時。これを実行すると、Actionsが、起動する。