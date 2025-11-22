import sqlite3
import os

def create_and_seed_database():
    """
    TemaPaletleri tablosunu oluşturur ve örnek verileri ekler.
    """
    DB_NAME = 'theme_palette.db'
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE TemaPaletleri (
                tema TEXT PRIMARY KEY,
                ana_ton_h INTEGER NOT NULL,
                anahtar_kelimeler TEXT NOT NULL
            )
        ''')
        print(f"[{DB_NAME}] TemaPaletleri tablosu başarıyla oluşturuldu.")

        
        tema_verileri = [
            ('Tutku', 0, 'aşk, sevgi,sevgili, hediye, gül, romantizm, kırmızı, kalp, tutku, ateş'),       # Kırmızı
            ('Doğa', 120, 'orman, ağaç, yeşil, doğa, bitki, çim, huzur'),           # Yeşil
            ('Sakinlik', 220, 'deniz, okyanus, gökyüzü, mavi, su, bulut, dingin'),  # Mavi
            ('Enerji', 45, 'güneş, hızlı, parlak, sarı, turuncu, canlı, ışık'),     # Turuncu/Sarı
            ('Gizem', 280, 'gece, mor, mistik, karanlık, rüya, gizem, sihir, cadı, büyü, orta çağ, süpürge, korkunç, hayalet'), #Mor
            ('Şehir', 0, 'tokyo, paris, istanbul, roma, rio, bali, ankara, pekin, madrid, moskova'),     # Sİyah
        ]

        
        for veri in tema_verileri:
            cursor.execute("INSERT INTO TemaPaletleri VALUES (?, ?, ?)", veri)
        
        conn.commit()
        print("Örnek veriler başarıyla eklendi.")

    except sqlite3.OperationalError:
        print("TemaPaletleri tablosu zaten mevcut.")
    except sqlite3.IntegrityError:
        print("Veriler zaten mevcut, atlandı.")

    conn.close()

if __name__ == "__main__":
    create_and_seed_database()
    print("\n Veritabanı Kurulumu Tamamlandı ")