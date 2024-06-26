# Potrebni biblioteki
import csv

# Kreiranje na rechnik vo koj gi definirame potrebnite promenlivi
# Promenlivite sodrzat podatok kakov shto nie ke mu dodelime
aplikant = {
    "ime_prezime": "\\",
    "vozrast": "\\",
    "pridones": "\\",
    "vrabotenost": "\\",
    "postoechki_kredit": "\\",
    "kredit": "\\",
    "staz": "\\",
    "meseci_za_plakanje": "\\",
    "zirant": "\\",
    "zirant_vozrast": "\\",
    "zirant_vrabotenost": "\\",
    "zirant_staz": "\\",
    "zirant_pridones": "\\",
    "hipoteka": "\\",
    "hipoteka_vrednost": "\\",
    "grad": "\\",
    "kredit_status": "\\"
}

# Updatnuva promenlivite vo rechnikot aplikant
def update_aplikant_data(key, value):
    if key in aplikant:
        aplikant[key] = value
    else:
        print(f"Key {key} not found in aplikant data.") #Vo sluchaj na greshka

# Pravilo 1 presmetka za score sprema vozrasta koja e vnesena od aplikantot
def score_vozrast(aplikant):
    vozrast = aplikant["vozrast"]
    if 18 <= vozrast <= 25:
        return 5
    elif 26 <= vozrast <= 60:
        return 10
    elif 61 <= vozrast <= 75:
        return 5
    else:  # vozrast >= 76
        return 0

# Pravilo 2 presmetka za score sprema pridonesot koj e vnesen od aplikantot
def score_pridones(aplikant):
    pridones = aplikant["pridones"]
    if pridones >= 22000:
        return 10
    elif 12000 <= pridones < 22000:
        return 0
    elif 0 < pridones < 12000:
        return -10
    else:  # pridones <= 0
        return -20

# Pravilo 3 presmetka za score ako e vraboten aplikantot
def score_vrabotenost(aplikant):
    vrabotenost = aplikant["vrabotenost"].lower()
    if vrabotenost == "da":
        return 10
    elif vrabotenost == "ne":
        return -10
    
# Pravilo 4 presmetka za score sprema stazot koj shto go ima aplikantot. 
def score_staz(aplikant):
    staz = aplikant["staz"]
    if staz is None:  # Ako aplikantot vnesi NE vo Pravilo 3
        return -10  
    elif staz < 1:
        return -5
    elif 1 <= staz <= 2:
        return 0
    else:
        return 10

# Pravilo 5 presmetka za score ako ima postoechki kredit
def score_postoechki_kredit(aplikant):
    postoechki_kredit = aplikant["postoechki_kredit"].lower()
    if postoechki_kredit == "da":
        return -10
    elif postoechki_kredit == "ne":
        return 10

# Pravilo 6 presmetka za score sprema vrednosta na kreditot koj  saka da ja podigne aplikantot
def score_kredit(aplikant):
    yearly_pridones = aplikant["pridones"] * 12
    kredit = aplikant["kredit"]
    if kredit <= (yearly_pridones * 0.3):
        return 10
    elif (yearly_pridones * 0.3) < kredit <= (yearly_pridones * 0.5):
        return 0
    else:
        return -10

# Pravilo 7 presmetka za score sprema vrednosta na kreditot koj  saka da ja podigne aplikantot
def score_meseci_za_plakanje(aplikant):
    kredit = aplikant["kredit"]
    meseci_za_plakanje = aplikant["meseci_za_plakanje"]
    pridones = aplikant["pridones"]
    monthly_repayment = kredit / meseci_za_plakanje
    remaining_pridones = pridones - monthly_repayment
    if remaining_pridones > 12000:
        return 10
    else:
        return -10

# Dopolnitelni prashanja vo sluchaj aplikantot da bidi blisku do odobruvanje na kreditot sprema negoviot score
# Sekoe prashanje ima ciklus while za proverka na podatocite koi gi vnesuva dali se soodvetni na prashanjeto    
def dopolnitelni_prashanja(aplikant):
    while True:
        zirant = input("Dali imate zirant? (Da/Ne): ").lower()
        if zirant in ["da", "ne"]:
            aplikant["zirant"] = zirant
            break
        else:
            print("Pogreshen vnes na podatok ve molime vnesete: Da/Ne.")
    if zirant == "da":
        while True:
            try:
                zirant_vozrast = int(input("Vnesete vozrast na zirantot: "))
                aplikant["zirant_vozrast"] = zirant_vozrast
                break
            except ValueError:
                print("Pogreshen vnes na podatok ve molime vnesete brojka za vozrast.")

        if zirant_vozrast >= 18:
            while True:
                zirant_vrabotenost = input("Dali zirantot e vraboten? (Da/Ne): ").lower()
                if zirant_vrabotenost in ["da", "ne"]:
                    aplikant["zirant_vrabotenost"] = zirant_vrabotenost
                    break
                else:
                    print("Pogreshen vnes na podatok ve molime vnesete: Da/Ne.")

            if zirant_vrabotenost == "da":
                while True:
                    try:
                        zirant_staz = int(input("Vnesete go stazot na vashiot zirant (vo godini): "))
                        aplikant["zirant_staz"] = zirant_staz
                        break
                    except ValueError:
                        print("Pogreshen vnes na podatok ve molime vnesete brojka za stazot na vashiot zirant.")

                while True:
                    try:
                        zirant_pridones = int(input("Vnesete go mesechniot pridones na vashiot zirant (vo denari): "))
                        aplikant["zirant_pridones"] = zirant_pridones
                        break
                    except ValueError:
                        print("Pogreshen vnes na podatok ve molime vnesete brojka za pridonesot na vashiot zirant.")
            else:
                aplikant["zirant_staz"] = 0
                aplikant["zirant_pridones"] = 0
        else:
            aplikant["zirant_vrabotenost"] = "ne"
            aplikant["zirant_staz"] = 0
            aplikant["zirant_pridones"] = 0
    else:
        aplikant["zirant_vozrast"] = 0
        aplikant["zirant_vrabotenost"] = "ne"
        aplikant["zirant_staz"] = 0
        aplikant["zirant_pridones"] = 0
    while True:
        hipoteka = input("Dali bi stavile neshto pod hipoteka? (da/Ne): ").lower()
        if hipoteka in ["da", "ne"]:
            aplikant["hipoteka"] = hipoteka
            break
        else:
            print("Pogreshen vnes na podatok ve molime vnesete: Da/Ne.")
    if hipoteka == "da":
        while True:
            try:
                hipoteka_vrednost = int(input("Vnesete ja vrednosta na hipotekata (vo denari): "))
                aplikant["hipoteka_vrednost"] = hipoteka_vrednost
                break
            except ValueError:
                print("Pogreshen vnes na podatok ve molime vnesete brojka za vrednosta na hipotekata.")
    else:
        aplikant["hipoteka_vrednost"] = 0

    return aplikant

# Dopolnitelni pravila

# Pravilo 8 presmetka na score za zirant
def score_zirant(aplikant):
    zirant = aplikant["zirant"].lower()
    if zirant == "da":
        zirant_vozrast = aplikant["zirant_vozrast"]
        if zirant_vozrast < 18:
            return 0
        zirant_vrabotenost = aplikant["zirant_vrabotenost"].lower()
        zirant_staz = aplikant["zirant_staz"]
        zirant_pridones = aplikant["zirant_pridones"]
        
        score = 0
        if zirant_vrabotenost == "da":
            if zirant_staz > 2:
                score += 10
            if zirant_pridones >= 22000:
                score += 10
            elif zirant_pridones < 22000:  
                score -= 10
        return score
    elif zirant == "ne":
        return 0
    else:
        return 0

# Pravilo 9 presmetka na score za hipoteka
def score_hipoteka(aplikant):
    hipoteka = aplikant["hipoteka"].lower()
    if hipoteka == "da":
        hipoteka_vrednost = aplikant["hipoteka_vrednost"]
        kredit = aplikant["kredit"]
        if hipoteka_vrednost >= kredit * 1.2:
            return 20
        else:
            return 0
    elif hipoteka == "ne":
        return 0
    else:
        return 0

# Kalkulacii na score sprema vnesenite podatoci i nosenje odluka 
def infer(aplikant):
    vozrast_score = score_vozrast(aplikant)
    
    scores = [
        vozrast_score,
        score_pridones(aplikant),
        score_vrabotenost(aplikant),
        score_postoechki_kredit(aplikant),
        score_kredit(aplikant),
        score_staz(aplikant),
        score_meseci_za_plakanje(aplikant)
    ]
    total_score = sum(scores)
    print(f"Vkupniot rezultat na {aplikant['ime_prezime']} e: {total_score}")
    if total_score > 30:
        aplikant["kredit_status"] = "Odobren"
        print(f"ODOBRENA e aplikacijata za kredit na {aplikant['ime_prezime']}")
    elif -10 < total_score <= 30:
        print(f"Dopolnitelni prashanja se potrebni za {aplikant['ime_prezime']}")
        aplikant = dopolnitelni_prashanja(aplikant)
        additional_scores = [
            score_zirant(aplikant),
            score_hipoteka(aplikant)
        ]
        total_score += sum(additional_scores)
        print(f"Vkupniot rezultat vkluchuvaj ki gi dopolnitelnite prashanja na {aplikant['ime_prezime']} e: {total_score}")
        if total_score > 30:
            aplikant["kredit_status"] = "Odobren"
            print(f"ODOBRENA e aplikacijata za kredit na {aplikant['ime_prezime']}")
        else:
            aplikant["kredit_status"] = "Odbien"
            print(f"ODBIENA e aplikacijata za kredit na {aplikant['ime_prezime']}")
    else:
        aplikant["kredit_status"] = "Odbien"
        print(f"ODBIENA e aplikacijata za kredit na {aplikant['ime_prezime']}")

# Korisnichki interfejs
# Sekoe prashanje ima ciklus while za proverka na podatocite koi gi vnesuva dali se soodvetni na prashanjeto 
def get_user_input():
    aplikant = {}  
    while True:
        ime_prezime = input("Vnesete ime i prezime: ")
        if all(x.isalpha() or x.isspace() for x in ime_prezime):
            aplikant["ime_prezime"] = ime_prezime
            break
        else:
            print("Pogreshen vnes na podatok ve molime vnesete bukvi za ime i prezime.")
    
    while True:
        try:
            vozrast = int(input("Vnesete vozrast: "))
            if vozrast < 18:
                # Ako aplikantot e pod 18 se pechati slednata odluka
                print("ODBIENA e aplikacijata za kredit. Prichina: Vozrast pod 18.")
                return  # Prekin na programata
            aplikant["vozrast"] = vozrast
            break
        except ValueError:
            print("Pogreshen vnes na podatok ve molime vnesete brojka za vozrast.")
    
    while True:
        grad = input("Vnesete grad: ")
        if grad.isalpha():
            aplikant["grad"] = grad
            break
        else:
            print("Pogreshen vnes na podatok ve molime vnesete bukvi za grad.")
    
    while True:
        try:
            aplikant["pridones"] = int(input("Vnesete mesechen pridones (vo denari): "))
            break
        except ValueError:
            print("Pogreshen vnes na podatok ve molime vnesete brojka za pridones.")

    if aplikant["pridones"] > 0:
        while True:
            vrabotenost = input("Dali ste vraboteni? (Da/Ne): ").lower()
            if vrabotenost in ["da", "ne"]:
                aplikant["vrabotenost"] = vrabotenost
                break
            else:
                print("Pogreshen vnes na podatok ve molime vnesete: Da/Ne.")
        
        if vrabotenost == "da":
            while True:
                try:
                    aplikant["staz"] = int(input("Vnesete staz (vo godini): "))
                    break
                except ValueError:
                    print("Pogreshen vnes na podatok ve molime vnesete brojka za stazot.")
        else:
            aplikant["staz"] = None
    else:
        aplikant["vrabotenost"] = "ne"
        aplikant["staz"] = None
    
    while True:
        postoechki_kredit = input("Dali imate postoechki kredit? (Da/Ne): ").lower()
        if postoechki_kredit in ["da", "ne"]:
            aplikant["postoechki_kredit"] = postoechki_kredit
            break
        else:
            print("Pogreshen vnes na podatok ve molime vnesete: Da/Ne.")
    
    while True:
        try:
            aplikant["kredit"] = int(input("Vnesete ja vrednosta na kreditot koj shto sakate da go podignete (vo denari): "))
            break
        except ValueError:
            print("Pogreshen vnes na podatok ve molime vnesete brojka za kreditot.")
    
    while True:
        try:
            aplikant["meseci_za_plakanje"] = int(input("Vnesete na kolku meseci bi go plakale kreditot: "))
            break
        except ValueError:
            print("Pogreshen vnes na podatok ve molime vnesete brojka za meseci na plakanje na kreditot.")

    return aplikant

# Zachuvuvanje na podatocite vneseni od aplikantot vo csv file
def save_to_csv(aplikant, filename="aplikant_data.csv"):
    # Promenlivite vo programata pretstaveni vo kolonite vo csv file
    field_mapping = {
        "ime_prezime": "Ime prezime",
        "vozrast": "Vozrast",
        "grad": "Grad",
        "pridones": "Pridones",
        "vrabotenost": "Vraboten",
        "staz": "Staz",
        "postoechki_kredit": "Postoechki kredit",
        "kredit": "Kredit",
        "meseci_za_plakanje": "Meseci za plakanje",
        "zirant": "Zirant",
        "zirant_vozrast": "Zirant vozrast",
        "zirant_vrabotenost": "Zirant vraboten",
        "zirant_staz": "Zirant staz",
        "zirant_pridones": "Zirant pridones",
        "hipoteka": "Hipoteka",
        "hipoteka_vrednost": "Hipoteka vrednost",
        "kredit_status": "Kredit status"
    }
    
    # Konvertiranje na promenlivite vo aplikant vo kolonite vo csv file
    csv_data = {field_mapping[key]: value for key, value in aplikant.items()}

    fieldnames = field_mapping.values()
    
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Ako se kreira prazen dokument da se popolnat iminjata na kolonite
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(csv_data)
        print(f"Applicant data saved to {filename}")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Glavna Programa
if __name__ == "__main__":
    print("CreditMaster")
    aplikant = get_user_input()
    if aplikant is not None:
        infer(aplikant)
        save_to_csv(aplikant)