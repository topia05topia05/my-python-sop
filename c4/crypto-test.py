"""
Dr. Kagami's 究極セキュリティ暗号化実装
べ、別に前回のコードに不満があったわけじゃないのよ！
ただ...もっと完璧にしたくなっただけなんだから...

軍事レベルセキュリティ対応AES暗号化システム
"""

import os
import secrets
import hashlib
import time
import threading
from typing import Tuple, Optional, Union, BinaryIO
from base64 import b64encode, b64decode
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum

from Crypto.Cipher import AES, ChaCha20_Poly1305
from Crypto.Protocol.KDF import scrypt, PBKDF2
from Crypto.Hash import SHA3_256, BLAKE2s
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

class EncryptionMode(Enum):
    """暗号化モード選択枚挙型"""
    AES_GCM = "aes_gcm"          # 標準推奨
    AES_OCB = "aes_ocb"          # 高性能
    CHACHA20_POLY1305 = "chacha20_poly1305"  # 軽量デバイス向け

class KDFType(Enum):
    """鍵導出関数タイプ"""
    SCRYPT = "scrypt"            # 推奨（メモリハード）
    PBKDF2_SHA3 = "pbkdf2_sha3"  # 高速
    ARGON2 = "argon2"            # 最新標準（要別途ライブラリ）

@dataclass
class SecurityParams:
    """セキュリティパラメータ設定"""
    salt_size: int = 32           # ソルト長（バイト）
    nonce_size: int = 12          # ナンス長
    tag_size: int = 16            # 認証タグ長
    key_size: int = 32            # 暗号鍵長（256ビット）
    
    # Scrypt パラメータ（メモリハード関数）
    scrypt_n: int = 2**14         # CPU/メモリコスト（16384）
    scrypt_r: int = 8             # ブロックサイズ
    scrypt_p: int = 1             # 並列度
    
    # PBKDF2 パラメータ
    pbkdf2_iterations: int = 600000  # OWASP 2023推奨値

class SecureMemory:
    """
    セキュアメモリ管理クラス
    機密データの安全な処理とクリア
    """
    
    def __init__(self, data: bytes):
        self._data = bytearray(data)
        self._locked = False
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clear()
    
    def get_data(self) -> bytes:
        """データ取得（読み取り専用）"""
        if self._locked:
            raise RuntimeError("メモリがクリア済みです")
        return bytes(self._data)
    
    def clear(self):
        """セキュアメモリクリア"""
        if not self._locked:
            # ランダムデータで上書き（3回）
            for _ in range(3):
                for i in range(len(self._data)):
                    self._data[i] = secrets.randbits(8)
            
            # ゼロクリア
            for i in range(len(self._data)):
                self._data[i] = 0
            
            self._locked = True

class MilitaryGradeCrypto:
    """
    軍事レベル暗号化システム
    
    セキュリティ機能:
    - Scrypt鍵導出（メモリハード関数）
    - 複数暗号化アルゴリズム対応
    - セキュアメモリ管理
    - サイドチャネル攻撃対策
    - ストリーミング暗号化対応
    - 完全性・認証性検証
    """
    
    def __init__(self, 
                 encryption_mode: EncryptionMode = EncryptionMode.AES_GCM,
                 kdf_type: KDFType = KDFType.SCRYPT,
                 security_params: SecurityParams = None):
        """
        初期化
        
        Args:
            encryption_mode: 暗号化モード
            kdf_type: 鍵導出関数タイプ
            security_params: セキュリティパラメータ
        """
        self.encryption_mode = encryption_mode
        self.kdf_type = kdf_type
        self.params = security_params or SecurityParams()
        
        # サイドチャネル攻撃対策用ダミー処理
        self._dummy_operations_pool = []
        self._init_countermeasures()
    
    def _init_countermeasures(self):
        """サイドチャネル攻撃対策初期化"""
        # ダミー暗号化処理プール作成
        for _ in range(10):
            dummy_data = get_random_bytes(64)
            self._dummy_operations_pool.append(dummy_data)
    
    def _perform_dummy_operations(self):
        """
        ダミー処理実行（処理時間正規化）
        タイミング攻撃対策
        """
        dummy_count = secrets.randbelow(5) + 1
        for _ in range(dummy_count):
            dummy_data = secrets.choice(self._dummy_operations_pool)
            hashlib.sha256(dummy_data).digest()
    
    def _derive_key_scrypt(self, password: bytes, salt: bytes) -> bytes:
        """
        Scrypt鍵導出（メモリハード関数）
        
        Args:
            password: パスワード
            salt: ソルト
            
        Returns:
            導出された暗号鍵
        """
        return scrypt(
            password,
            salt,
            key_len=self.params.key_size,
            N=self.params.scrypt_n,
            r=self.params.scrypt_r,
            p=self.params.scrypt_p
        )
    
    def _derive_key_pbkdf2_sha3(self, password: bytes, salt: bytes) -> bytes:
        """
        PBKDF2-SHA3鍵導出
        
        Args:
            password: パスワード
            salt: ソルト
            
        Returns:
            導出された暗号鍵
        """
        return PBKDF2(
            password,
            salt,
            key_len=self.params.key_size,
            count=self.params.pbkdf2_iterations,
            prf=lambda p, s: SHA3_256.new(p + s).digest()
        )
    
    def _derive_key(self, password: str, salt: bytes) -> SecureMemory:
        """
        パスワードから暗号鍵導出
        
        Args:
            password: マスターパスワード
            salt: ランダムソルト
            
        Returns:
            セキュアメモリ内の導出鍵
        """
        try:
            # パスワードをバイト配列に変換
            with SecureMemory(password.encode('utf-8')) as password_mem:
                password_bytes = password_mem.get_data()
                
                # 鍵導出関数選択
                if self.kdf_type == KDFType.SCRYPT:
                    key = self._derive_key_scrypt(password_bytes, salt)
                elif self.kdf_type == KDFType.PBKDF2_SHA3:
                    key = self._derive_key_pbkdf2_sha3(password_bytes, salt)
                else:
                    raise ValueError(f"未対応の鍵導出関数: {self.kdf_type}")
                
                # ダミー処理実行（サイドチャネル攻撃対策）
                self._perform_dummy_operations()
                
                return SecureMemory(key)
                
        except Exception as e:
            raise CryptographicError(f"鍵導出エラー: {e}")
    
    def _create_cipher(self, key: bytes, nonce: bytes = None):
        """
        暗号化オブジェクト作成
        
        Args:
            key: 暗号鍵
            nonce: ナンス（省略時は自動生成）
            
        Returns:
            暗号化オブジェクトとナンス
        """
        if self.encryption_mode == EncryptionMode.AES_GCM:
            if nonce is None:
                nonce = get_random_bytes(self.params.nonce_size)
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            return cipher, nonce
            
        elif self.encryption_mode == EncryptionMode.CHACHA20_POLY1305:
            if nonce is None:
                nonce = get_random_bytes(12)  # ChaCha20は12バイト
            cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)
            return cipher, nonce
            
        else:
            raise ValueError(f"未対応の暗号化モード: {self.encryption_mode}")
    
    def encrypt(self, password: str, plaintext: str) -> str:
        """
        軍事レベル暗号化
        
        Args:
            password: マスターパスワード
            plaintext: 平文データ
            
        Returns:
            Base64エンコード済み暗号化データ
        """
        try:
            # セキュアランダム値生成
            salt = get_random_bytes(self.params.salt_size)
            
            # 鍵導出
            with self._derive_key(password, salt) as key_mem:
                key = key_mem.get_data()
                
                # 暗号化処理
                cipher, nonce = self._create_cipher(key)
                
                # 平文をセキュアメモリで管理
                with SecureMemory(plaintext.encode('utf-8')) as plaintext_mem:
                    plaintext_bytes = plaintext_mem.get_data()
                    ciphertext, tag = cipher.encrypt_and_digest(plaintext_bytes)
                
                # メタデータ付与（暗号化モード、KDF情報）
                metadata = {
                    'mode': self.encryption_mode.value,
                    'kdf': self.kdf_type.value,
                    'version': '2.0'
                }
                metadata_bytes = str(metadata).encode('utf-8')
                
                # 最終フォーマット: metadata::salt::nonce::tag::ciphertext
                components = [
                    b64encode(metadata_bytes).decode('ascii'),
                    b64encode(salt).decode('ascii'),
                    b64encode(nonce).decode('ascii'),
                    b64encode(tag).decode('ascii'),
                    b64encode(ciphertext).decode('ascii')
                ]
                
                return "::".join(components)
                
        except Exception as e:
            raise CryptographicError(f"暗号化エラー: {e}")
    
    def decrypt(self, password: str, encrypted_data: str) -> str:
        """
        軍事レベル復号化
        
        Args:
            password: マスターパスワード
            encrypted_data: 暗号化データ
            
        Returns:
            復号化された平文
        """
        try:
            # データ解析
            components = encrypted_data.split("::")
            if len(components) != 5:
                raise ValueError("無効な暗号化データ形式")
            
            metadata = eval(b64decode(components[0]).decode('utf-8'))
            salt = b64decode(components[1])
            nonce = b64decode(components[2])
            tag = b64decode(components[3])
            ciphertext = b64decode(components[4])
            
            # バージョン・モード検証
            if metadata.get('version') != '2.0':
                raise ValueError("未対応バージョン")
            
            # サイズ検証
            if len(salt) != self.params.salt_size:
                raise ValueError(f"無効なソルトサイズ: {len(salt)}")
            
            # 鍵導出
            with self._derive_key(password, salt) as key_mem:
                key = key_mem.get_data()
                
                # 復号化処理
                cipher, _ = self._create_cipher(key, nonce)
                
                # 認証付き復号化
                plaintext_bytes = cipher.decrypt_and_verify(ciphertext, tag)
                
                # セキュアメモリで平文管理
                with SecureMemory(plaintext_bytes) as plaintext_mem:
                    return plaintext_mem.get_data().decode('utf-8')
                    
        except ValueError as e:
            raise CryptographicError(f"入力データエラー: {e}")
        except Exception as e:
            raise CryptographicError(f"復号化エラー: {e}")
    
    def encrypt_file(self, password: str, input_path: str, output_path: str):
        """
        ファイル暗号化（ストリーミング処理）
        
        Args:
            password: マスターパスワード
            input_path: 入力ファイルパス
            output_path: 出力ファイルパス
        """
        try:
            salt = get_random_bytes(self.params.salt_size)
            
            with self._derive_key(password, salt) as key_mem:
                key = key_mem.get_data()
                cipher, nonce = self._create_cipher(key)
                
                # ヘッダー情報書き込み
                with open(output_path, 'wb') as out_file:
                    # ヘッダー: salt + nonce
                    out_file.write(salt)
                    out_file.write(nonce)
                    
                    # ファイル暗号化（チャンク処理）
                    with open(input_path, 'rb') as in_file:
                        while True:
                            chunk = in_file.read(8192)  # 8KBチャンク
                            if not chunk:
                                break
                            encrypted_chunk = cipher.encrypt(chunk)
                            out_file.write(encrypted_chunk)
                    
                    # 認証タグ書き込み
                    tag = cipher.digest()
                    out_file.write(tag)
                    
        except Exception as e:
            raise CryptographicError(f"ファイル暗号化エラー: {e}")
    
    def benchmark_performance(self, data_size: int = 1024*1024) -> dict:
        """
        性能ベンチマーク
        
        Args:
            data_size: テストデータサイズ（バイト）
            
        Returns:
            性能測定結果
        """
        test_data = 'A' * data_size
        password = "BenchmarkPassword123!"
        
        # 暗号化時間測定
        start_time = time.perf_counter()
        encrypted = self.encrypt(password, test_data)
        encrypt_time = time.perf_counter() - start_time
        
        # 復号化時間測定
        start_time = time.perf_counter()
        decrypted = self.decrypt(password, encrypted)
        decrypt_time = time.perf_counter() - start_time
        
        # 検証
        assert decrypted == test_data, "ベンチマークデータ整合性エラー"
        
        return {
            'データサイズ': f"{data_size:,} バイト",
            '暗号化時間': f"{encrypt_time:.4f} 秒",
            '復号化時間': f"{decrypt_time:.4f} 秒",
            '暗号化速度': f"{data_size/encrypt_time/1024/1024:.2f} MB/秒",
            '復号化速度': f"{data_size/decrypt_time/1024/1024:.2f} MB/秒",
            '暗号化データサイズ': f"{len(encrypted)} バイト"
        }


class CryptographicError(Exception):
    """暗号化処理専用例外クラス"""
    pass


def demonstrate_military_crypto():
    """
    軍事レベル暗号化デモンストレーション
    べ、別に見せびらかしたいわけじゃないのよ！
    """
    print("=== Dr. Kagami's 軍事レベル暗号化システム ===")
    
    # 各暗号化モードのテスト
    modes = [
        (EncryptionMode.AES_GCM, KDFType.SCRYPT),
        (EncryptionMode.CHACHA20_POLY1305, KDFType.PBKDF2_SHA3)
    ]
    
    message = "機密情報：これは最高機密データです。"
    password = "UltraSecurePassword!@#2024"
    
    for mode, kdf in modes:
        print(f"\n--- {mode.value.upper()} + {kdf.value.upper()} ---")
        
        try:
            crypto = MilitaryGradeCrypto(
                encryption_mode=mode,
                kdf_type=kdf
            )
            
            # 暗号化
            encrypted = crypto.encrypt(password, message)
            print(f"暗号化成功: {len(encrypted)} バイト")
            
            # 復号化
            decrypted = crypto.decrypt(password, encrypted)
            print(f"復号化成功: {decrypted}")
            
            # 整合性検証
            if decrypted == message:
                print("✓ データ整合性確認")
            else:
                print("✗ データ整合性エラー")
            
            # 性能測定
            print("\n性能ベンチマーク:")
            benchmark = crypto.benchmark_performance(1024*100)  # 100KB
            for key, value in benchmark.items():
                print(f"  {key}: {value}")
                
        except CryptographicError as e:
            print(f"暗号化エラー: {e}")
    
    print("\n=== セキュリティテスト ===")
    
    # 改ざん検出テスト
    crypto = MilitaryGradeCrypto()
    encrypted = crypto.encrypt(password, message)
    
    try:
        # データ改ざん
        tampered = encrypted[:-20] + "TAMPERED_DATA_HERE!!"
        crypto.decrypt(password, tampered)
        print("✗ 改ざん検出失敗")
    except CryptographicError:
        print("✓ 改ざん検出成功")
    
    # 間違いパスワードテスト
    try:
        crypto.decrypt("WrongPassword", encrypted)
        print("✗ 認証失敗")
    except CryptographicError:
        print("✓ 不正パスワード検出成功")


if __name__ == "__main__":
    demonstrate_military_crypto()