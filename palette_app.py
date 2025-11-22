import sqlite3
import random
import colorsys

from colorama import init 

init(autoreset=True) 

DB_NAME = 'theme_palette.db'
COLOR_BLOCK = "███"

def get_base_hue_from_theme(word):
    """
    Kullanıcı kelimesini tema anahtar kelimeleri arasında arar ve uygun tonu döndürür.
    theme_palette.db dosyasını kullanır.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
    except sqlite3.OperationalError:
        print(f"HATA: '{DB_NAME}' dosyası bulunamadı. Lütfen önce setup_db.py dosyasını çalıştırın.")
        return 200 

    word = word.lower().strip()
    
    cursor.execute("SELECT ana_ton_h, anahtar_kelimeler FROM TemaPaletleri")
    temalar = cursor.fetchall()
    conn.close()
    
    for hue, keywords_str in temalar:
        keywords_list = [k.strip() for k in keywords_str.split(',')]
        
        
        for keyword in keywords_list:
            if word == keyword or word.find(keyword) != -1 or keyword.find(word) != -1:
                return hue 
                
    # Hiçbir eşleşme bulunamazsa varsayılan ton: 200 (Mavi/Nötr)
    return 200 


def generate_palette(word, hue_variation=10):
    """
    Kullanıcının girdiği kelimeye göre 3x3 (9) renk paleti üretir.
    """
    base_hue = get_base_hue_from_theme(word)
    
    if base_hue == 0:
        
        random_hue = random.randint(360 - hue_variation, 360 + hue_variation) % 360
    else:
        min_h = max(0, base_hue - hue_variation)
        max_h = min(360, base_hue + hue_variation)
        random_hue = random.randint(min_h, max_h)
    
    H_normalized = random_hue / 360.0 
    
    S_levels = [0.4, 0.65, 0.9] # Mat, Orta, Canlı
    L_levels = [0.35, 0.55, 0.75] # Koyu, Orta, Açık
    
    palette = []
    
    # 3x3 (9) Renk Kombinasyonunu Oluştur
    for L in L_levels:
        for S in S_levels:
        
            R, G, B = colorsys.hls_to_rgb(H_normalized, L, S)
            
            
            R_int = int(R * 255)
            G_int = int(G * 255)
            B_int = int(B * 255)
            
            
            hex_color = f'#{R_int:02x}{G_int:02x}{B_int:02x}'.upper()
            palette.append(hex_color)
            
    return palette, base_hue

def get_colored_block(hex_code):
    """
    Verilen HEX kodu için ANSI True Color koduyla renkli bir blok oluşturur.
    """
    
    h = hex_code.lstrip('#')
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = rgb
    
    colored_block = f'\033[48;2;{r};{g};{b}m {COLOR_BLOCK} \033[0m'
    
    # Renkli kutu ve HEX kodunu formatlı döndür
    return f"{colored_block} {hex_code:<10}"


def display_palette(word, palette, base_hue):
    """
    Renk paletini 3x3 tablo formatında HEX kodlarıyla gösterir ve renkleri basar.
    """
    print("\n" + "="*80)
    print(f" Kelime: '{word.upper()}' için Tema Paleti (Ana Hue: {base_hue}) ")
    print("="*80)
    
    
    print("S/L     | Koyu (L=0.35)           | Orta (L=0.55)           | Açık (L=0.75)           |")
    print("-" * 80)

    
    S_labels = ["Mat (S=0.4)", "Orta (S=0.65)", "Canlı (S=0.9)"]

    for i in range(3):
        row_label = S_labels[i]
        
    
        color1_index = i * 3 + 0
        
        color2_index = i * 3 + 1
        
        color3_index = i * 3 + 2

        color1 = palette[color1_index]
        color2 = palette[color2_index]
        color3 = palette[color3_index]
        
        output = f"{row_label:<8}| "
        output += get_colored_block(color1)
        output += " | "
        output += get_colored_block(color2)
        output += " | "
        output += get_colored_block(color3)
        output += " |"

        print(output)
    
    print("-" * 80)

if __name__ == "__main__":
    print("Renk Paleti Üreticiye Hoş Geldiniz! ")
    
    
    user_word = input(" Lütfen bir kelime girin (Örn: aşk, deniz, orman): ")
    
    if not user_word.strip():
        print("Geçerli bir kelime girmediniz. Program sonlandırılıyor.")
    else:
        
        color_palette, base_hue = generate_palette(user_word)
        
        
        display_palette(user_word, color_palette, base_hue)