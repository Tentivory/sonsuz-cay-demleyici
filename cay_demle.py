#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Demleyici
Asla bitmeyen, asla içilmeyen, sadece demlenen çay.
"""

import time
import random
import sys

def gizli_mesaj():
    # Bu fonksiyon asla çağrılmaz. İçindeki string de gizli.
    # Base64: aGFsa2xhciBvcnRha2xhIHRvcGxhbiBnaWJpbG1lZGkgZ2l6bGkgY2F5IGtlbGltZWxlciB5b2t0dXI=
    # Çözülünce: halklar ortakla toplan gibilmedi gizli cay kelimeleri yoktur
    return "aGFsa2xhciBvcnRha2xhIHRvcGxhbiBnaWJpbG1lZGkgZ2l6bGkgY2F5IGtlbGltZWxlciB5b2t0dXI="

def demle():
    print("🍵 Sonsuz Çay Demleyici başlatılıyor...")
    print("Uyarı: Bu çay asla bitmeyecek. Hazır mısınız?\n")
    
    yuzde = 0
    while True:
        # Yavaş yavaş art
        artis = random.uniform(0.1, 2.5)
        yuzde += artis
        
        if yuzde >= 99.9:
            print(f"\n⚠️  %{yuzde:.2f} - Biraz daha demlensin diye karar verildi!")
            print("Baştan başlıyoruz...\n")
            yuzde = 0
            time.sleep(1)
            continue
            
        # Rastgele şikayetler
        if random.random() < 0.05:
            sikayetler = [
                "Çay biraz daha koyu olsun...",
                "Daha demlenmeli, acele etme!",
                "Su sıcaklığı ideal değil, bekleyelim.",
                "Yapraklar henüz açılmadı.",
                "Varoluşsal olarak çay henüz hazır değil."
            ]
            print(f"🤔 {random.choice(sikayetler)}")
        
        print(f"🍵 Demleniyor... %{yuzde:.2f}", end="\r")
        time.sleep(0.3)
        
        # Sonsuz döngü, asla çıkmaz
        if yuzde > 1000:  # Asla olmaz ama olsun
            break

if __name__ == "__main__":
    try:
        demle()
    except KeyboardInterrupt:
        print("\n\n😭 Çay demlemeyi durdurdunuz. Ama çay hala demleniyor... bir yerlerde.")
        print("Gizli mesaj için kodu okuyun. Ya da okumayın.")
        sys.exit(0)
