#Key_generator.py

import os
import hashlib
import time
import base64
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class ProfessionalKeyGenerator:
    def __init__(self):
        # .env içindeki MY_APP_SALT değerini kullanır
        self.salt = os.getenv("MY_APP_SALT", "varsayilan_yedek_tuz_degeri")

    def collatz_entropy(self, n):
        """
        Collatz dizisini kullanarak karmaşık bir sayısal veri üretir.
        """
        sequence = []
        while n > 1:
            sequence.append(str(n))
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        sequence.append("1")
        # Diziyi birleştirip hash için hazır hale getirir
        return "".join(sequence).encode()

    def generate_secure_key(self, length=32):
        # 1. ADIM: Donanımsal Rastgelelik
        random_bytes = os.urandom(64)
        
        # 2. ADIM: Zaman Faktörü
        timestamp_ns = time.time_ns()
        timestamp_bytes = str(timestamp_ns).encode()
        
        # 3. ADIM: Collatz Algoritması (YENİ)
        # Zamanın son hanelerini kullanarak bir başlangıç sayısı oluşturur
        collatz_seed = (timestamp_ns % 100000) + 1
        collatz_data = self.collatz_entropy(collatz_seed)
        
        # 4. ADIM: Hepsini Harmanla
        # Rastgele Veri + Zaman + Collatz Dizisi + Gizli Tuz
        hash_input = random_bytes + timestamp_bytes + collatz_data + self.salt.encode()
        
        # SHA-256 ile özetle
        secure_hash = hashlib.sha256(hash_input).digest()
        
        # Base64 formatına çevir
        key = base64.urlsafe_b64encode(secure_hash).decode('utf-8')
        
        return key[:length]

# Kullanım
if __name__ == "__main__":
    generator = ProfessionalKeyGenerator()
    new_key = generator.generate_secure_key(24)

    print(f"--- Collatz Destekli Güvenli Anahtar ---")
    print(f"Key: {new_key}")
    print(f"Uzunluk: {len(new_key)} karakter")