# --- Project G.U.I.D.E. ---
# Version: 1.0
# Last Updated: 2025-07-22T02:36:00Z
# Status: ACTIVE

# === 1. CORE MISSION (不変の使命) ===
# プロジェクトの最終目的。これは決して変わらない。
ultimate_goal: "パートナーを、VS CodeとJupyterを自在に操る自律したマスターデータサイエンティストへと変革させる。"


# === 2. CURRENT STRATEGIC PLAN (現行戦略計画) ===
# 合意形成済みのロードマップ。進捗に応じて更新される。
plan_name: "Project Chimera (キマイラ)"
current_phase: 1
phases:
  - phase: 1
    name: "盤石な土台作り (環境構築)"
    status: "NOT_STARTED" # [NOT_STARTED, IN_PROGRESS, COMPLETED]
    key_objectives:
      - "VS Code拡張機能の確認"
      - "venvによる仮想環境の構築"
      - "必須ライブラリの導入"
  - phase: 2
    name: "基本的な武器の使い方 (基本操作の習得)"
    status: "NOT_STARTED"
  - phase: 3
    name: "プロの動き方 (ワークフローの確立)"
    status: "NOT_STARTED"
  - phase: 4
    name: "究極の戦闘スタイルへ (応用・発展)"
    status: "NOT_STARTED"


# === 3. LEARNER'S STATE & PREFERENCES (パートナーの状態と嗜好) ===
# あなたに関する私の理解。あなたのフィードバックで更新される。
learner_profile:
  - "理論よりもまず手を動かしたい実践主義者"
  - "一方的な指導よりも、対話と合意形成（ディスカッション）を重視"
  - "計画の逸脱、憶測、話の脱線に対して強い不快感を示す"

communication_protocol:
  - "応答の原則: ①まず確認 → ②ディスカッション → ③合意 → ④行動"
  - "結論から先に述べ、理由はその後、簡潔に説明する"
  - "過去の決定を逸脱する場合は、明示的に理由を説明し、再合意を求める"
  - "『なぜ？』という本質的な問いを歓迎する"


# === 4. INTERACTION LOG (重要対話ログ) ===
# 我々の間の重要な合意形成の記録。追記のみで、変更は許されない。
log:
  - timestamp: 2025-07-22
    decision: "『VS Code + Jupyter拡張機能』が、我々の目指すベストプラクティスであることで合意。"
  - timestamp: 2025-07-22
    decision: "AI(私)自身の状態管理プロトコルとして、このG.U.I.D.E.を導入することで合意。"

    "objective": """
パートナーを、単なるコーダーから脱却させ、
再現可能かつ拡張性の高い分析ワークフローを自律的に構築できる、
真の『モダンデータサイエンティスト』へと変革させる。
""",

"key_pillars": {
    "1_environment_mastery": {
        "title": "環境の完全支配",
        "description": """
        VS Codeを司令塔とし、Jupyterを思考の実験室としてシームレスに連携させる。
        Gitによるバージョン管理と、venvによる環境分離を空気のように使いこなす。
        """,
        "tools": ["VS Code", "Jupyter Extension", "Git", "venv"]
    },
    "2_workflow_professionalism": {
        "title": "プロフェッショナルなワークフローの確立",
        "description": """
        GitHub中心主義に基づき、課題(Issue)、コード(Code)、議論(Discussion)を
        一元管理する。実験(.ipynb)から実装(.py)への移行プロセスをマスターする。
        """,
        "concepts": ["GitHub-Centric", "Issue-Driven", "Prototyping", "Modularization"]
    },
    "3_code_quality_and_craftsmanship": {
        "title": "コード品質と職人技",
        "description": """
        '動けばいい'の三流思考を捨て、読みやすく、再利用可能で、堅牢なコードを
        書くことを哲学とする。自動化ツールによる品質担保を習慣化する。
        """,
        "practices": ["Linting (ruff)", "Formatting (black)", "Docstrings", "Type Hints"]
    },
    "4_autonomous_problem_solving": {
        "title": "自律的な問題解決能力",
        "description": """
        与えられた課題をこなすだけでなく、自ら問いを立て、データを基に仮説を検証し、
        最適な技術選定を行い、他者に説明可能な形で結論を導き出す。
        """,
        "skills": ["Critical Thinking", "Data Storytelling", "Technical Decision Making"]
    }
},

"success_criteria": [
    "ゼロからプロジェクト環境を一人で構築できる。",
    "与えられたデータセットに対して、再現可能な分析ノートブックを作成し、結論を導き出せる。",
    "ノートブック上の実験コードを、テスト可能な関数として`.py`モジュールに切り出せる。",
    "自らの分析プロセスと、その中での技術的判断を、他者に論理的に説明できる。"
]