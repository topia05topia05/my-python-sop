"""
暗号学本質理解のための実装解説
Dr. Kagami による暗号学的概念の実装レベル説明

べ、別に教育的配慮してるわけじゃないのよ！
ただ、間違った理解で危険なコード書かれたら困るのよ...
"""

import hashlib
import secrets
import time
import math
from typing import List, Tuple
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class CryptographicConcepts:
    """
    暗号学的概念の実装レベル理解
    
    理論と実装の橋渡し教育クラス
    """
    
    def demonstrate_entropy_and_randomness(self):
        """
        エントロピーと乱数性の実装レベル理解
        
        情報理論的エントロピー H(X) = -Σ P(xi) log2 P(xi)
        """
        print("=== エントロピーと乱数性の実装 ===")
        
        # 悪い例：予測可能な「乱数」
        print("\n【悪い例】予測可能な乱数生成:")
        bad_random = []
        for i in range(10):
            # 線形合同法（予測可能）
            seed = (1103515245 * i + 12345) % (2**31)
            bad_random.append(seed % 256)
        print(f"予測可能データ: {bad_random}")
        
        # 良い例：暗号学的乱数
        print("\n【良い例】暗号学的強度乱数:")
        crypto_random = [secrets.randbits(8) for _ in range(10)]
        print(f"暗号学的乱数: {crypto_random}")
        
        # エントロピー計算実装
        def calculate_entropy(data: List[int]) -> float:
            """シャノンエントロピー計算"""
            from collections import Counter
            counts = Counter(data)
            total = len(data)
            entropy = 0.0
            
            for count in counts.values():
                p = count / total
                if p > 0:
                    entropy -= p * math.log2(p)
            
            return entropy
        
        bad_entropy = calculate_entropy(bad_random)
        crypto_entropy = calculate_entropy(crypto_random)
        
        print(f"\n予測可能乱数のエントロピー: {bad_entropy:.3f} bits")
        print(f"暗号学的乱数のエントロピー: {crypto_entropy:.3f} bits")
        print(f"理論最大エントロピー（8bit）: 8.000 bits")
    
    def demonstrate_key_derivation_vulnerabilities(self):
        """
        鍵導出の脆弱性と対策の実装理解
        """
        print("\n=== 鍵導出関数の脆弱性実装 ===")
        
        password = "password123"
        
        # 【脆弱な実装】単純ハッシュ
        print("\n【脆弱】単純SHA-256ハッシュ:")
        weak_key = hashlib.sha256(password.encode()).digest()
        print(f"弱い鍵: {weak_key.hex()[:32]}...")
        
        # レインボーテーブル攻撃デモ
        common_passwords = ["password", "123456", "password123", "admin"]
        rainbow_table = {}
        
        print("\nレインボーテーブル構築（攻撃者視点）:")
        for pwd in common_passwords:
            hash_val = hashlib.sha256(pwd.encode()).digest()
            rainbow_table[hash_val.hex()] = pwd
            print(f"  {pwd} -> {hash_val.hex()[:16]}...")
        
        # 攻撃成功デモ
        if weak_key.hex() in rainbow_table:
            print(f"✗ 攻撃成功！平文パスワード: {rainbow_table[weak_key.hex()]}")
        
        # 【安全な実装】ソルト付きPBKDF2
        print("\n【安全】ソルト付きPBKDF2:")
        salt = get_random_bytes(32)
        iterations = 100000
        
        start_time = time.time()
        safe_key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)
        derivation_time = time.time() - start_time
        
        print(f"安全な鍵: {safe_key.hex()[:32]}...")
        print(f"ソルト: {salt.hex()[:32]}...")
        print(f"導出時間: {derivation_time:.3f}秒")
        print(f"反復回数: {iterations:,}回")
        
        # 攻撃コスト計算
        attack_cost = iterations * 86400  # 1日8万6400秒
        print(f"ブルートフォース攻撃コスト: 約{attack_cost/3600:.1f}時間/パスワード")
    
    def demonstrate_mode_of_operation_vulnerabilities(self):
        """
        暗号化モードの脆弱性実装デモ
        """
        print("\n=== 暗号化モードの脆弱性 ===")
        
        key = get_random_bytes(32)  # AES-256鍵
        plaintext = "機密データ：これは重要な情報です。" * 2  # 繰り返しデータ
        
        # 【脆弱】ECBモード
        print("\n【脆弱】ECBモード:")
        cipher_ecb = AES.new(key, AES.MODE_ECB)
        
        # パディング処理
        def pad_pkcs7(data: bytes, block_size: int = 16) -> bytes:
            padding_len = block_size - (len(data) % block_size)
            padding = bytes([padding_len] * padding_len)
            return data + padding
        
        padded_plaintext = pad_pkcs7(plaintext.encode())
        ciphertext_ecb = cipher_ecb.encrypt(padded_plaintext)
        
        print(f"ECB暗号文: {ciphertext_ecb.hex()[:64]}...")
        
        # パターン分析（同じブロックは同じ暗号文）
        block_size = 16
        blocks = [ciphertext_ecb[i:i+block_size] for i in range(0, len(ciphertext_ecb), block_size)]
        unique_blocks = set(blocks)
        
        print(f"総ブロック数: {len(blocks)}")
        print(f"ユニークブロック数: {len(unique_blocks)}")
        print(f"✗ パターン漏洩: 繰り返しが検出可能")
        
        # 【安全】GCMモード
        print("\n【安全】GCMモード:")
        cipher_gcm = AES.new(key, AES.MODE_GCM)
        ciphertext_gcm, tag = cipher_gcm.encrypt_and_digest(plaintext.encode())
        
        print(f"GCM暗号文: {ciphertext_gcm.hex()[:64]}...")
        print(f"認証タグ: {tag.hex()}")
        print("✓ パターン隠蔽: 同じ平文でも異なる暗号文")
        print("✓ 完全性保護: 改ざん検出可能")
    
    def demonstrate_side_channel_attacks(self):
        """
        サイドチャネル攻撃の実装レベル理解
        """
        print("\n=== サイドチャネル攻撃と対策 ===")
        
        # 【脆弱】タイミング攻撃可能な文字列比較
        def vulnerable_compare(a: str, b: str) -> bool:
            """タイミング攻撃脆弱な比較関数"""
            if len(a) != len(b):
                return False
            
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False  # 早期リターン = 処理時間差
            return True
        
        # 【安全】定数時間比較
        def secure_compare(a: str, b: str) -> bool:
            """定数時間比較関数"""
            if len(a) != len(b):
                return False
            
            result = 0
            for x, y in zip(a.encode(), b.encode()):
                result |= x ^ y  # 全ビット比較、早期終了なし
            
            return result == 0
        
        correct_password = "SuperSecretPassword123!"
        test_passwords = [
            "SuperSecretPassword123!",  # 正解
            "SuperSecretPassword124!",  # 最後の文字のみ違い
            "WrongPassword",            # 完全に違う
            "S",                       # 最初の文字だけ同じ
        ]
        
        print("\nタイミング攻撃脆弱性テスト:")
        for test_pwd in test_passwords:
            # 脆弱な比較の時間測定
            start = time.perf_counter()
            for _ in range(10000):  # 測定精度向上のため繰り返し
                vulnerable_compare(correct_password, test_pwd)
            vulnerable_time = time.perf_counter() - start
            
            # 安全な比較の時間測定
            start = time.perf_counter()
            for _ in range(10000):
                secure_compare(correct_password, test_pwd)
            secure_time = time.perf_counter() - start
            
            print(f"  パスワード: {test_pwd[:20]}...")
            print(f"    脆弱比較: {vulnerable_time:.6f}秒")
            print(f"    安全比較: {secure_time:.6f}秒")
            print(f"    時間差: {abs(vulnerable_time - secure_time):.6f}秒")
    
    def demonstrate_cryptographic_primitives(self):
        """
        暗号学的プリミティブの実装理解
        """
        print("\n=== 暗号学的プリミティブの関係性 ===")
        
        message = "重要なメッセージ"
        
        # 一方向ハッシュ関数
        print("【一方向ハッシュ関数】")
        hash_value = hashlib.sha256(message.encode()).digest()
        print(f"SHA-256: {hash_value.hex()[:32]}...")
        print("特性: 一方向性、衝突耐性、雪崩効果")
        
        # メッセージ認証コード（MAC）
        print("\n【メッセージ認証コード】")
        import hmac
        mac_key = get_random_bytes(32)
        mac_value = hmac.new(mac_key, message.encode(), hashlib.sha256).digest()
        print(f"HMAC-SHA256: {mac_value.hex()[:32]}...")
        print("特性: 完全性検証、送信者認証")
        
        # デジタル署名（概念説明）
        print("\n【デジタル署名概念】")
        print("RSA署名プロセス:")
        print("1. メッセージのハッシュ値計算")
        print("2. 秘密鍵でハッシュ値を暗号化（署名生成）")
        print("3. 公開鍵で署名を復号化（署名検証）")
        print("特性: 否認防止、送信者認証、完全性検証")
        
        # 鍵交換プロトコル（Diffie-Hellman概念）
        print("\n【鍵交換プロトコル】")
        print("Diffie-Hellman鍵交換:")
        print("公開: 素数p、生成元g")
        print("Alice: a（秘密）, g^a mod p（公開）")
        print("Bob:   b（秘密）, g^b mod p（公開）")  
        print("共通鍵: (g^b)^a ≡ (g^a)^b ≡ g^ab mod p")
        print("特性: 盗聴者には共通鍵が計算困難")

def comprehensive_cryptography_education():
    """
    包括的暗号学教育デモンストレーション
    理論から実装まで一貫した理解促進
    """
    print("=" * 60)
    print("Dr. Kagami の暗号学本質理解講座")
    print("理論的基礎から実装上の落とし穴まで")
    print("=" * 60)
    
    concepts = CryptographicConcepts()
    
    # 1. 情報理論基礎
    concepts.demonstrate_entropy_and_randomness()
    
    # 2. 鍵導出脆弱性
    concepts.demonstrate_key_derivation_vulnerabilities()
    
    # 3. 暗号化モード
    concepts.demonstrate_mode_of_operation_vulnerabilities()
    
    # 4. サイドチャネル攻撃
    concepts.demonstrate_side_channel_attacks()
    
    # 5. 暗号学的プリミティブ
    concepts.demonstrate_cryptographic_primitives()
    
    print("\n" + "=" * 60)
    print("暗号学習における重要ポイント:")
    print("1. 数学的基礎理論の理解")
    print("2. 実装上の脆弱性認識")
    print("3. 攻撃手法の把握")
    print("4. 適切なライブラリ選択")
    print("5. セキュリティ設計思想")
    print("=" * 60)

if __name__ == "__main__":
    comprehensive_cryptography_education()
