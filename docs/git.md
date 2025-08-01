# Git - 操作手順 & トラブルシューティング

---
## 基本操作

| コマンド | 解説 |
|:---|:---|
| `git init` | **リポジトリの初期化:** カレントディレクトリを、Gitの、管理下に置く。初回のみ。 |
| `git status` | **現状確認:** 前回の、記録からの、変更点を、表示する。常に、使う、癖をつけなさい。 |
| `git add .` | **ステージング:** 全ての、変更を、次の、記録の、対象にする。 |
| `git commit -m "msg"`| **ローカル記録:** ステージングされた、変更を、`msg`という、メッセージ付きで、自分のPCに、記録する。 |
| `git push` | **リモート公開:** ローカルに、記録した、変更を、GitHubに、送信する。 |
| `git pull` | **リモート取得:** GitHub上の、最新の、変更を、自分のPCに、取り込む。 |

---
## トラブルシューティング

| 問題 | 解決策 |
|:---|:---|
| コミットメッセージを、<br>修正したい | `git commit --amend -m "新しいメッセージ"` |
| `add`を、取り消したい | `git reset HEAD <ファイル名>` |
| 最新の、コミットを、<br>取り消したい | `git reset --soft HEAD~1` (変更内容は、残る) |
| `push`が、拒否される | `git pull` を、実行し、リモートの変更を取り込んでから、再度、`push`する。 |