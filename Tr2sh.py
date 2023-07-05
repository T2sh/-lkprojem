modern_sozluk = { "LOL":"sesli gulmek", "ROFL":"gulmekten yere donmek", "CRINGE":"Utandirici"}

soru = input("Hangi kelimenin anlami ogrenmek istiyorsun?")

soru = soru.upper()

if soru in modern_sozluk.keys():
    print(modern_sozluk[soru])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Kelime bulunmadi!")
