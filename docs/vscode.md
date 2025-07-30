# VS Code - ワークフロー & TIPS

---
## 日々の、ワークフロー

### 作業開始フロー (Pre-Flight Checklist)
| ステップ | 操作 / コマンド | 解説 |
|:---:|:---|:---|
| 1 | `Ctrl + @` | 統合ターミナルを、開く。 |
| 2 | `.venv\Scripts\activate` | ターミナルで、仮想環境を、有効化する。 |

### 作業終了フロー (Post-Flight Checklist)
| ステップ | 操作 / コマンド | 解説 |
|:---:|:---:|:---|
| 1 | `deactivate` | ターミナルで、仮想環境を、無効化する。 |

---
## TIPS / 初回設定

| 操作 / コマンド | 解説 |
|:--- |:--- |
| `python -m venv .venv` | **[初回のみ]** 新しい、プロジェクトで、仮想環境を、作成する。 |
| `Ctrl + Shift + P` | **[随時]** コマンドパレットを、開く。`Select Interpreter`など、VS Codeの、全機能を、検索・実行できる。 |

---
## トラブルシューティング

| 問題 | 解決策 |
|:--- |:--- |
| 仮想環境(.venv)が、<br>自動で、認識されない | 1. `Ctrl+Shift+P` > `Python: Select Interpreter` を実行する。<br>2. リストから、手動で、`.venv\Scripts\python.exe` を選択する。 |