# seymencan
import requests

while True:
    print("\n----- Crawler -----")
    choice = input("-s (subdomain), -d (dizin), exit (çıkış) > ")

    if choice == "exit":
        break

    # Tüm inputları çeker
    target = input("Hedef URL (örn: example.com): ")
    filepath = input("Wordlist dosyasının yolunu girin: ")

    print("\n--- Tarama Başladı (" + target + ") ---")

    # Memory check yapar
    # Error responsive olmayacak, var olmayan bir url girilirse program kapanacak
    file = open(filepath, "r")
    wordlist = file.readlines()
    file.close() 

    
    for word in wordlist:
        
        clean_word = word.replace("\n", "")

        # boş satır varsa geç
        if clean_word == "":
            continue

        if choice == "-s":
            url = "https://" + clean_word + "." + target
            response = requests.get(url)
            if response.status_code == 200:
                print("[+] SEYMENCAN Buldu: " + url)

        elif choice == "-d":
            # ful URL exportla
            url = "https://www." + target + "/" + clean_word
            response = requests.get(url)
            if response.status_code == 404:
                print("[+] SEYMENCAN: " + url)

    print("--- Tarama Bitti ---")
