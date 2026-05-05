import random
import sys

# ============================================================
#               GENERATORE NPC v5.3 - STABILE (EOF FIXED)
# ============================================================

NAMES = ["Jax", "Akira", "Zane", "Liara", "Kai", "Nova", "Echo", "Ren", "Sora", "Dimitri",
         "Ivan", "Sergei", "Alexei", "Nikolai", "Yuri", "Diego", "Mateo", "Javier", "Carlos", "Sofia",
         "Isabella", "Elena", "Carmen", "Kwame", "Amara", "Zuri", "Jamal", "Aisha", "Malik", "Tariq",
         "Fatima", "Omar", "Neo", "Zero", "Blaze", "Vortex", "Pixel", "Cipher", "Quantum", "Flux",
         "Shadow", "Ghost", "Razor", "Bolt", "Spark", "Chrome", "Neon", "Pulse", "Byte", "Grid",
         "Void", "Nexus", "Apex", "Titan", "Phantom", "Specter", "Orion", "Vega", "Sirius", "Lyra",
         "Mira", "Elara", "Thorne", "Raven", "Storm", "Frost", "Ember", "Ash", "Slate", "Onyx",
         "Quartz", "Cobalt", "Indigo", "Violet", "Crimson", "Azure", "Jade", "Ruby", "Opal", "Pearl",
         "Hiro", "Yuki", "Kenji", "Aiko", "Haruto", "Mei", "Wei", "Li", "Chen", "Zhang",
         "Liu", "Wang", "Petrov", "Ivanov", "Smirnov", "Rodriguez", "Hernandez", "Lopez", "Kim", "Patel"]

SURNAMES = ["Kaito", "Ramirez", "Chen", "Ivanov", "Sato", "Patel", "Al-Rashid", "Okafor", "Dubois",
            "Nakamura", "Rodriguez", "Kim", "Singh", "Mbeki", "Al-Farsi", "Hernandez", "Lopez", "Moreau",
            "Takahashi", "Volkov", "Delgado", "Hassan", "Okoro", "Bianchi", "Yamamoto", "Kuznetsov", "Morales", "Ndiaye",
            "Kren", "Vex", "Thorne", "Slate", "Onyx", "Cobalt", "Indigo", "Crimson", "Azure", "Jade",
            "Ruiz", "Khan", "Mensah", "Okeke", "Diallo", "Traore", "Ba", "Diop", "Niang", "Fall"]

NICKNAMES = ["Neon Ghost", "Chrome Reaper", "Data Phantom", "Void Runner", "Pulse King", "Shadow Broker",
             "Iron Saint", "Net Witch", "Blade Phantom", "Corp Slayer", "Zero Hour", "Gridlock",
             "Cyber Siren", "Razor Queen", "Byte Bandit", "Neon Viper", "Storm Chaser", "Echo Hunter"]

ARCHETYPES = [
    {"name": "Street Samurai", "desc": "Guerriero con codice"},
    {"name": "Corporate Insider", "desc": "Ex-dipendente con segreti"},
    {"name": "Black Market Dealer", "desc": "Specialista contrabbando"},
    {"name": "Cybernetic Enforcer", "desc": "Braccio armato"},
    {"name": "Data Thief", "desc": "Ladro di dati"},
    {"name": "Pilot/Spacer", "desc": "Esperto di navi"},
    {"name": "Underground Medic", "desc": "Medico clandestino"},
    {"name": "Rebel Leader", "desc": "Visionario ribelle"},
    {"name": "Corporate Assassin", "desc": "Killer professionista"},
    {"name": "AI Whisperer", "desc": "Parla con le IA"},
]

PERSONALITIES = [
    {"tratto": "Paranoid", "desc": "Diffida di tutti"},
    {"tratto": "Ruthless", "desc": "Sacrifica chiunque"},
    {"tratto": "Idealistic", "desc": "Crede in un futuro migliore"},
    {"tratto": "Cynical", "desc": "Non si fida di nessuno"},
    {"tratto": "Charismatic", "desc": "Attira follower"},
    {"tratto": "Greedy", "desc": "Tutto ha un prezzo"},
    {"tratto": "Curious", "desc": "Non resiste ai misteri"},
    {"tratto": "Vengeful", "desc": "Ricorda ogni torto"},
    {"tratto": "Playful", "desc": "Tratta la morte come gioco"},
    {"tratto": "Stoic", "desc": "Emozioni = vulnerabilità"},
]

TRATTI_FISICI = [
    "Cicatrice che attraversa l’occhio sinistro", "Occhio destro completamente nero", "Tatuaggio che copre metà del viso",
    "Capelli rasati con disegni geometrici", "Protesi al posto di un orecchio", "Voce leggermente metallica",
    "Mani insolitamente grandi", "Pelle molto pallida o molto scura", "Occhi di due colori diversi",
    "Cicatrici multiple sul collo", "Denti affilati o dorati", "Andatura leggermente zoppicante",
    "Mani costantemente sporche di olio", "Sguardo molto intenso o vuoto", "Capelli lunghi e spettinati",
    "Pelle con venature luminose", "Voce molto bassa o molto acuta", "Braccio sinistro più muscoloso",
    "Cicatrice a forma di fulmine sul viso", "Occhi che cambiano leggermente colore",
    "Tatuaggi che coprono entrambe le braccia", "Postura rigida o eccessivamente rilassata",
    "Pelle con piccole cicatrici da ustione", "Dita insolitamente lunghe",
    "Sguardo che evita il contatto visivo", "Capelli tinti di colori innaturali",
    "Voce con leggero eco", "Braccio destro coperto da placche metalliche",
    "Pelle con macchie scure", "Andatura felina o aggressiva",
    "Cicatrice che divide le sopracciglia", "Mani sempre fredde",
    "Sguardo che sembra leggere dentro le persone", "Capelli molto corti o completamente rasati",
    "Voce rauca o roca", "Protesi visibile su una gamba",
    "Pelle con leggere luminescenze", "Espressione facciale quasi sempre neutra",
    "Mani con calli molto evidenti", "Sguardo che sorride anche quando la bocca no"
]

VESTIARIO = [
    "Tuta da pilota stealth", "Giacca con LED integrati", "Cappotto olografico retrattile",
    "Armatura leggera mimetica", "Tuta synthweave rinforzata", "Giubbotto con placche balistiche",
    "Cappuccio con visore notturno", "Tuta da lavoro intera", "Giacca con tasche multiple",
    "Abito elegante cyberpunk", "Tuta mimetica urbana", "Cappotto con cappuccio termico",
    "Giubbotto tattico modulare", "Tuta da combattimento leggera", "Abito con inserti luminosi",
    "Cappotto lungo con LED", "Tuta da tecnico con tasche", "Giacca con rinforzi metallici",
    "Tuta intera nera opaca", "Cappuccio con proiettore olografico", "Armatura leggera da campo",
    "Giacca con strisce riflettenti", "Tuta da pilota con patch", "Cappotto pesante termico",
    "Abito elegante sdrucito"
]

VISIBLE_DAMAGE = ["Nessun danno evidente"] * 25 + [
    "Cicatrice da laser sottile", "Ustione chimica sul braccio", "Impianto guasto con scintille",
    "Cicatrice da proiettile", "Protesi danneggiata con cavi esposti", "Ustione da sovraccarico neurale",
    "Cicatrice da coltello vibro", "Impianto oculare crepato", "Pelle con vene nere",
    "Cicatrice da esplosione", "Protesi con placca arrugginita", "Tatuaggio bruciato",
    "Impianto spinale malfunzionante", "Cicatrice da morso di drone", "Pelle con macchie luminescenti",
    "Protesi con giuntura bloccata", "Cicatrice da frusta monofilamento", "Impianto con perdita di fluido",
    "Ustione da plasma", "Cicatrice da sparo ravvicinato", "Protesi con vernice scrostata",
    "Segni di graffi profondi", "Impianto con LED malfunzionanti", "Cicatrice da coltello termico",
    "Danno grave multiplo"
]

ROLES = [
    "Hacker/Netrunner", "Smuggler", "Bounty Hunter", "Corporate Fixer", "Explorer/Scout",
    "Mercenary", "Cyberdoc", "Pilot/Spacer", "Technician/Engineer", "Data Broker",
    "Rebel/Insurgent", "Cultist/Mystic", "Trader/Merchant", "Security Officer", "Scientist/Researcher",
    "Assassin/Shadow Operative", "Diplomat/Negotiator", "Scavenger/Salvager", "AI Specialist/Synth Whisperer", "Debt Collector/Enforcer"
]

SKILLS = {
    "PHYSICAL": ["Might", "Agility", "Endurance"],
    "TECH": ["Medicine", "Engineering"],
    "DIGITAL": ["Browsing", "Hacking"],
    "PILOT": ["Spaceship", "Vehicle"],
    "SURVIVAL": ["Senses", "Tracking"],
    "SOCIAL": ["Cunning", "Fear", "Mannerism"],
    "WEAPONS": ["Melee", "Explosives", "Ranged"],
    "LORE": ["Science", "History", "Investigation", "Linguistics"]
}

ARMORS = [
    {"name": "Reinforced Clothing", "ap": 1},
    {"name": "Armor Vest", "ap": 4},
    {"name": "Standard Infantry Armor", "ap": 7},
    {"name": "Powered Infantry Armor", "ap": 14},
    {"name": "Subdermal Armor", "ap": 0},
]

WEAPONS = [
    {"name": "Combat Knife", "dmg": "1d5+MDM"},
    {"name": "Autopistol", "dmg": "1d10+1"},
    {"name": "Revolver", "dmg": "1d10+3"},
    {"name": "Hand Cannon", "dmg": "1d10+2"},
    {"name": "Assault Rifle", "dmg": "2d10+2"},
    {"name": "Pulse Rifle", "dmg": "3d10"},
    {"name": "Pump Shotgun", "dmg": "3d10/1d10+3"},
    {"name": "Sniper Rifle", "dmg": "3d10"},
    {"name": "Flamethrower", "dmg": "2d10 (AA)"},
]

DEVASTATING_WEAPONS = [
    {"name": "Railgun Sniper", "dmg": "4d10"},
    {"name": "Smart Rifle", "dmg": "4d10"},
    {"name": "Heavy Plasma Cannon", "dmg": "4d10"},
]

TRINKETS = ["Ciondolo con foto sbiadita", "Accendino cromato consumato", "Chiave USB logora", "Collana con dente di drago", "Orologio rotto con data incisa", "Flacone di pillole vuote", "Piccolo drone rotto", "Carta da gioco con bordo dorato", "Flacone di profumo costoso", "Moneta antica con foro", "Piccolo coltello pieghevole", "Scheda di memoria con canzoni", "Anello con pietra nera", "Kit di riparazione per droni", "Lettera sigillata mai aperta", "Flacone di stimolanti", "Piccolo specchio incrinato", "Chiave di una vecchia astronave", "Pacchetto di sigarette elettroniche", "Piccolo libro di poesie cyberpunk", "Braccialetto con codice QR", "Flacone di lubrificante per protesi", "Dado a 20 facce consumato", "Piccolo flacone di acqua santa", "Scheda di accesso rubata", "Collana con dente di lupo", "Piccolo registratore vocale", "Flacone di crema rigenerante", "Chiave inglese antica", "Piccolo portafortuna a forma di sole", "Flacone di feromoni sintetici", "Piccolo libro di codici cifrati", "Braccialetto con luci LED", "Flacone di pillole per il sonno", "Piccolo coltello da lancio", "Scheda di memoria con foto di famiglia", "Flacone di lubrificante per armature", "Piccolo drone da compagnia (rotto)", "Lettera d'amore mai spedita", "Flacone di stimolanti da combattimento", "Piccolo specchio con incisione", "Chiave di un deposito segreto", "Flacone di profumo", "Piccolo libro di preghiere IA", "Braccialetto con sensore di salute", "Flacone di antidoto generico", "Piccolo coltello da combattimento", "Scheda di memoria con diario vocale", "Flacone di crema per cicatrici", "Piccolo drone da sorveglianza (rotto)", "Collana con croce di neon", "Flacone di stimolanti mentali", "Piccolo libro di ricette di strada", "Braccialetto con codice di accesso", "Flacone di lubrificante per protesi", "Piccolo coltello da combattimento bilanciato", "Scheda di memoria con mappe segrete", "Flacone di antidolorifici forti", "Piccolo drone da compagnia (funzionante)", "Lettera di dimissioni mai spedita", "Flacone di feromoni da combattimento", "Piccolo libro di codici morse", "Braccialetto con sensore di radiazioni", "Flacone di crema rigenerante avanzata", "Piccolo coltello da lancio bilanciato", "Scheda di memoria con registrazioni segrete", "Flacone di lubrificante per droni", "Piccolo libro di poesie perdute", "Braccialetto con luci di emergenza", "Flacone di antidoto specifico", "Piccolo drone da ricognizione (rotto)", "Lettera di addio mai letta", "Flacone di lubrificante per armature pesanti", "Piccolo coltello da sopravvivenza", "Scheda di memoria con mappe di Capital", "Flacone di stimolanti da hacking", "Piccolo libro di preghiere per IA", "Braccialetto con sensore di stress", "Flacone di crema per ustioni", "Piccolo drone da compagnia (avanzato)", "Lettera di ricatto mai spedita", "Flacone di stimolanti da combattimento avanzati", "Piccolo libro di codici antichi", "Braccialetto con luci di segnalazione", "Flacone di antidoto universale", "Piccolo coltello da combattimento bilanciato", "Scheda di memoria con diari di guerra", "Flacone di lubrificante per droni", "Piccolo libro di ricette di strada avanzate", "Braccialetto con sensore di radiazioni avanzato", "Flacone di crema rigenerante sperimentale", "Piccolo drone da sorveglianza avanzato", "Lettera di dimissioni firmata", "Flacone di stimolanti mentali avanzati", "Piccolo libro di codici di sicurezza", "Braccialetto con luci di emergenza avanzate", "Flacone di antidoto sperimentale", "Piccolo coltello da lancio bilanciato avanzato", "Scheda di memoria con registrazioni segrete avanzate", "Flacone di stimolanti da combattimento sperimentali"]

BACKGROUNDS = [
    {"name": "Ex-Corporate", "desc": "Ex-dipendente di una mega-corp", "bonus": "+2 LORE"},
    {"name": "Street Rat", "desc": "Cresciuto nei bassifondi", "bonus": "+2 SURVIVAL"},
    {"name": "Ex-Soldato", "desc": "Veterano di guerre corporative", "bonus": "+2 WEAPONS"},
    {"name": "Underground Hacker", "desc": "Ex-membro di un collettivo hacker", "bonus": "+3 DIGITAL"},
    {"name": "Scavenger Pro", "desc": "Professionista del recupero", "bonus": "+3 SURVIVAL"},
    {"name": "Pilot Smuggler", "desc": "Trasportatore illegale", "bonus": "+3 PILOT"},
    {"name": "Corporate Defector", "desc": "Fuggito da una mega-corp", "bonus": "+2 LORE + 1 SOCIAL"},
    {"name": "Rebel Sympathizer", "desc": "Supporta un movimento ribelle", "bonus": "+2 SOCIAL"},
    {"name": "Synth Whisperer", "desc": "Specialista nel trattare con IA", "bonus": "+3 LORE"},
    {"name": "Black Market Fixer", "desc": "Mediatore del mercato nero", "bonus": "+3 SOCIAL"},
    {"name": "Ex-Security Officer", "desc": "Ex-guardia di una Capital", "bonus": "+2 WEAPONS"},
    {"name": "Street Doctor", "desc": "Medico senza licenza", "bonus": "+3 TECH (Medicine)"},
    {"name": "Corporate Assassin (Ritirato)", "desc": "Ex-killer professionista", "bonus": "+3 WEAPONS"},
    {"name": "Data Broker", "desc": "Venditore di informazioni", "bonus": "+3 DIGITAL"},
    {"name": "Synth Companion", "desc": "Ex-compagno sintetico", "bonus": "+2 SOCIAL + 1 LORE"},
    {"name": "Grid Rat", "desc": "Cresciuto in un Patch", "bonus": "+2 TECH + 1 SURVIVAL"},
    {"name": "Ex-Cult Member", "desc": "Ex-membro di setta techno-religiosa", "bonus": "+2 LORE + 1 SOCIAL"},
    {"name": "Debt Collector", "desc": "Ex-recuperatore di debiti", "bonus": "+2 SOCIAL + 1 WEAPONS"},
    {"name": "Deep Spacer", "desc": "Ha passato anni nello spazio", "bonus": "+3 PILOT + 1 SURVIVAL"},
    {"name": "Information Broker", "desc": "Specialista nel raccogliere segreti", "bonus": "+3 LORE"},
]

ALLINEAMENTI = [
    {"name": "Corporate Loyalist", "desc": "Fedele alle mega-corporazioni"},
    {"name": "Rebel Anarchist", "desc": "Vuole abbattere il sistema"},
    {"name": "Neutral Scavenger", "desc": "Sopravvive a tutti i costi"},
    {"name": "Lawful Enforcer", "desc": "Rispetta le regole del potere"},
    {"name": "Chaotic Opportunist", "desc": "Fa quello che gli conviene"},
    {"name": "Idealist Visionary", "desc": "Cerca un mondo migliore"},
]

# ====================== VARIABILI GLOBALI ======================
current_power_range = None
current_role_pref = None

POWER_RANGES = {
    "debole": (1, 6),
    "competente": (6, 12),
    "forte": (12, 18),
    "minaccia": (18, 20)
}

# ====================== FUNZIONI ======================

def calculate_debt(power, role):
    base = power // 2
    mod = 0
    if any(x in role for x in ["Corporate", "Fixer", "Assassin"]): mod = random.randint(5, 7)
    elif any(x in role for x in ["Mercenary", "Bounty", "Shadow"]): mod = random.randint(3, 5)
    elif any(x in role for x in ["Pilot", "Cyberdoc", "Technician"]): mod = random.randint(2, 4)
    elif any(x in role for x in ["Scavenger", "Rebel", "Smuggler"]): mod = random.randint(-3, 1)
    return max(0, min(20, base + mod))

def get_debt_status(debt):
    if debt <= 4: return "Libero o protetto"
    elif debt <= 9: return "Precario ma gestibile"
    elif debt <= 14: return "Intrappolato"
    else: return "Proprietà del sistema"

def generate_equipment(role, power, background, category):
    if power >= 14 and random.random() < 0.35:
        armor = {"name": "Subdermal Armor", "ap": power // 2}
    else:
        armor = random.choice([a for a in ARMORS if a["name"] != "Subdermal Armor"])
        armor = armor.copy()
        armor["ap"] = power

    if power > 15 and random.random() < 0.55:
        weapon = random.choice(DEVASTATING_WEAPONS)
    else:
        weapon = random.choice(WEAPONS)

    extra = []
    if power >= 12: extra.append("500 creds")
    if power >= 16: extra.append("Drone da ricognizione")
    if "Hacker" in role or "Data Broker" in role: extra.append("Neural Deck")
    if "Pilot" in role: extra.append("Navicomputer")
    if category == "Combat": extra.append("Medkit da campo")
    if category == "Scum": extra.append("Toolkit da infiltrazione")
    if category == "Civilian": extra.append("Toolkit professionale")
    if category == "Support": extra.append("long range comms")
    if category == "Navigator" extra.append("drone da ricognizione")

    return armor, weapon, extra

def generate_npc():
    global current_power_range, current_role_pref

    if current_power_range:
        low, high = POWER_RANGES[current_power_range]
        power = random.randint(low, high)
    else:
        power = random.randint(1, 20)

    if current_role_pref:
        category = current_role_pref
    else:
        category = random.choice(["Civilian", "Combat", "Scum"])

    is_android = random.random() < 0.07
    if is_android:
        category = "Android"

    role = random.choice(ROLES)
    arch = random.choice(ARCHETYPES)
    pers = random.choice(PERSONALITIES)
    background = random.choice(BACKGROUNDS)
    allineamento = random.choice(ALLINEAMENTI)

    full_name = f'"{random.choice(NICKNAMES)}" {random.choice(NAMES)} {random.choice(SURNAMES)}'
    age = random.randint(19, 67)
    sex = random.choice(["Maschio", "Femmina", "Non-binario"])
    pronouns = {"Maschio": "he/him", "Femmina": "she/her", "Non-binario": "they/them"}[sex]

    tratti_fisici = random.sample(TRATTI_FISICI, 3)

    dmg_roll = random.randint(26, 50) if (category in ["Combat", "Technician"] and random.random() < 0.65) else random.randint(1, 50)
    visible_damage = VISIBLE_DAMAGE[dmg_roll - 1]

    debt = calculate_debt(power, role)
    debt_status = get_debt_status(debt)

    body = min(85 if power < 15 else 95, 35 + power * 2 + random.randint(-5, 8))
    speed = min(85 if power < 15 else 95, 35 + power * 2 + random.randint(-5, 8))
    intellect = min(85 if power < 15 else 95, 35 + power * 2 + random.randint(-5, 8))
    combat = min(85 if power < 15 else 95, 15 + power * 2)
    hits = 1 + (power // 5)

    skills_str = []
    for cat, subs in list(SKILLS.items())[:4]:
        for sub in subs[:2]:
            val = min(85 if power < 15 else 95, 20 + power * 2 + random.randint(-8, 12))
            skills_str.append(f"{cat[:3]}({sub[:3]}):+{val}")

    armor, weapon, extra = generate_equipment(role, power, background, category)
    trinket = random.choice(TRINKETS)

    android_note = " [ANDROIDE]" if is_android else ""

    output = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║ {full_name} | {age} anni | {sex} ({pronouns}){android_note}
║ {category} / {role} | Potenza: {power} | Allineamento: {allineamento['name']}
╠══════════════════════════════════════════════════════════════════════════════╣
║ Background     : {background['name']} — {background['desc']}
║ Bonus          : {background['bonus']}
╠══════════════════════════════════════════════════════════════════════════════╣
║ Visible Damage : {visible_damage}
║ Debito         : {debt} ({debt_status})
╠══════════════════════════════════════════════════════════════════════════════╣
║ Hits: {hits} | Body: {body} | Speed: {speed} | Intellect: {intellect} | Combat: +{combat}
╠══════════════════════════════════════════════════════════════════════════════╣
║ Skills: {', '.join(skills_str)}
╠══════════════════════════════════════════════════════════════════════════════╣
║ Tratti Fisici  : {', '.join(tratti_fisici)}
║ Vestiario      : {random.choice(VESTIARIO)}
╠══════════════════════════════════════════════════════════════════════════════╣
║ EQUIPAGGIAMENTO
║ Armor  : {armor['name']} (AP {armor['ap']})
║ Weapon : {weapon['name']} ({weapon['dmg']} DMG)
║ Extra  : {', '.join(extra) if extra else 'Nessun extra'}
║ Trinket: {trinket}
╠══════════════════════════════════════════════════════════════════════════════╣
║ Flavor: {pers['desc']}. {arch['desc']}.
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    return output

# ====================== MAIN ======================
if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                    GENERATORE NPC v5.3 - STABILE (EOF FIXED)                 ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝\n")
    print("Comandi: debole / competente / forte / minaccia / civilian / combat / scum / reset\n")

    while True:
        print(f"Impostazioni attuali → Potenza: {current_power_range or 'casuale'} | Preferenza: {current_role_pref or 'casuale'}")

        try:
            cmd = input("Comando o Invio per generare: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            cmd = ""

        if cmd in POWER_RANGES:
            current_power_range = cmd
            print(f"→ Range potenza impostato: {cmd.upper()}")
        elif cmd in ["civilian", "combat", "scum"]:
            current_role_pref = cmd
            print(f"→ Preferenza ruolo impostata: {cmd.upper()}")
        elif cmd == "reset":
            current_power_range = None
            current_role_pref = None
            print("→ Impostazioni ripristinate")
        else:
            print(generate_npc())

            try:
                again = input("\nGenerare un altro NPC? (s/n): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                break
            if again != "s":
                print("\nGrazie per aver usato il generatore!")
                break