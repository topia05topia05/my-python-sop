# 【改善版】Dr. Kagami's Secure Encryption
# 必要なライブラリをインポートするわよ。ちゃんとインストールしておきなさい。
# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import json # 複数のデータを扱うなら、区切り文字よりJSONの方が堅牢よ

# --- 定数 ---
# こうやって定数化しておくと、後から変更するのが楽になるの。基本よ。
SALT_SIZE = 16
KEY_BYTES = 16  # AES-128だから16バイト (128 bit)
PBKDF2_ITERATIONS = 100000 # ストレッチングの回数。多いほど安全だけど遅くなるわ。

def encrypt(password: str, data: str) -> str:
    """
    パスワードとデータから、安全な暗号化テキストを生成するわ。
    KDFを使って、パスワードからセキュアな鍵を導出するのがポイントよ。
    """
    # 1. ソルト(Salt)を生成する。毎回ランダムなものを使うことで、同じパスワードでも違う鍵が生成されるの。
    salt = get_random_bytes(SALT_SIZE)
    
    # 2. PBKDF2を使って、パスワードとソルトから安全な鍵を生成する。これが一番大事！
    key = PBKDF2(password, salt, dkLen=KEY_BYTES, count=PBKDF2_ITERATIONS)
    
    # 3. AES (EAXモード)で暗号化。nonceは自動で生成されるわ。
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    
    # 4. 必要なデータを全部まとめる。辞書にしてからJSONにするのがスマートなやり方。
    encrypted_data = {
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8'),
        'ciphertext': b64encode(ciphertext).decode('utf-8')
    }
    
    return json.dumps(encrypted_data)

def decrypt(password: str, encrypted_json: str) -> str:
    """
    暗号化されたJSONから、元のデータを復号するわ。
    暗号化時と全く同じ手順で鍵を再生成する必要があるのよ。
    """
    # 1. JSONをパースして、各パーツを取り出す
    try:
        b64_data = json.loads(encrypted_json)
        salt = b64decode(b64_data['salt'])
        nonce = b64decode(b64_data['nonce'])
        tag = b64decode(b64_data['tag'])
        ciphertext = b64decode(b64_data['ciphertext'])
    except (ValueError, KeyError) as e:
        # エラーハンドリングは必須よ！
        raise ValueError("不正な暗号データ、あるいは破損している可能性があります。") from e

    # 2. 暗号化時と同じソルトとパスワード、設定で鍵を"再"生成する
    key = PBKDF2(password, salt, dkLen=KEY_BYTES, count=PBKDF2_ITERATIONS)
    
    # 3. 復号オブジェクトを生成し、データの復元と検証を同時に行う
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
        return decrypted_data.decode('utf-8')
    except ValueError:
        # タグの検証に失敗した場合、データが改ざんされたか、パスワードが間違っているということ
        # これがEAXモードの「封蝋」が機能した証拠よ！
        raise ValueError("復号に失敗しました。パスワードが違うか、データが改ざんされています。")

# __name__ はアンダースコア2つよ！忘れないで！
if __name__ == '__main__':
    message = "自分がしてほしいと思うことを人にもするように。"
    password = "a-much-stronger-and-secret-password" # パスワードはもっと複雑にしなさい！

    print("--- 安全な暗号化プロセス ---")
    encrypted = encrypt(password, message)
    print("暗号化:", encrypted)
    
    decrypted = decrypt(password, encrypted)
    print("復号化:", decrypted)

    print("\n--- わざと失敗させてみるわ ---")
    try:
        # 間違ったパスワードで復号を試みる
        decrypt("wrong-password", encrypted)
    except ValueError as e:
        print("案の定、エラーが出たわね:", e)