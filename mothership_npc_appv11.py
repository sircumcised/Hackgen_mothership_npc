import streamlit as st
import random

st.set_page_config(page_title="Mothership NPC Generator v5.6", page_icon="🪐", layout="wide")

# ============================================================
#  DATI (compatte e ottimizzate)
# ============================================================

NAMES = ["Jax", "Akira", "Zane", "Liara", "Kai", "Nova", "Echo", "Ren", "Sora", "Dimitri", "Ivan", "Sergei", "Alexei", "Nikolai", "Yuri", "Diego", "Mateo", "Javier", "Carlos", "Sofia", "Isabella", "Elena", "Carmen", "Kwame", "Amara", "Zuri", "Jamal", "Aisha", "Malik", "Tariq", "Fatima", "Omar", "Neo", "Zero", "Blaze", "Vortex", "Pixel", "Cipher", "Quantum", "Flux", "Shadow", "Ghost", "Razor", "Bolt", "Spark", "Chrome", "Neon", "Pulse", "Byte", "Grid", "Void", "Nexus", "Apex", "Titan", "Phantom", "Specter", "Orion", "Vega", "Sirius", "Lyra", "Mira", "Elara", "Thorne", "Raven", "Storm", "Frost", "Ember", "Ash", "Slate", "Onyx", "Quartz", "Cobalt", "Indigo", "Violet", "Crimson", "Azure", "Jade", "Ruby", "Opal", "Pearl", "Hiro", "Yuki", "Kenji", "Aiko", "Haruto", "Mei", "Wei", "Li", "Chen", "Zhang", "Liu", "Wang", "Petrov", "Ivanov", "Smirnov", "Rodriguez", "Hernandez", "Lopez", "Kim", "Patel", "Kael", "Vesper", "Draven", "Nyx", "Riven", "Sable", "Corvin", "Liora", "Thal", "Veyra", "Korr", "Sylas", "Mirael", "Drax", "Elyndra", "Vorath", "Seraph", "Kaelith", "Nyxara", "Vael"]

SURNAMES = ["Kaito", "Ramirez", "Chen", "Ivanov", "Sato", "Patel", "Al-Rashid", "Okafor", "Dubois", "Nakamura", "Rodriguez", "Kim", "Singh", "Mbeki", "Al-Farsi", "Hernandez", "Lopez", "Moreau", "Takahashi", "Volkov", "Delgado", "Hassan", "Okoro", "Bianchi", "Yamamoto", "Kuznetsov", "Morales", "Ndiaye", "Kren", "Vex", "Thorne", "Slate", "Onyx", "Cobalt", "Indigo", "Crimson", "Azure", "Jade", "Ruiz", "Khan", "Mensah", "Okeke", "Diallo", "Traore", "Ba", "Diop", "Niang", "Fall", "Voss", "Krell", "Drake", "Shadow", "Vex", "Corvus", "Nyx", "Riven", "Sable", "Thorne", "Vael", "Korr", "Sylas", "Vorath", "Seraph", "Kaelith", "Nyxara", "Elyndra", "Mirael", "Drax"]

NICKNAMES = ["Neon Ghost", "Chrome Reaper", "Data Phantom", "Void Runner", "Pulse King", "Shadow Broker", "Iron Saint", "Net Witch", "Blade Phantom", "Corp Slayer", "Zero Hour", "Gridlock", "Cyber Siren", "Razor Queen", "Byte Bandit", "Neon Viper", "Storm Chaser", "Echo Hunter", "Blackout", "Voidwalker", "Corpse Whisperer", "Null Signal", "Deadlight", "Iron Veil", "Wraith", "Specter-9", "Hollow Man", "Eclipse", "Grimwire", "Bonejack", "Silent Protocol", "Ashwalker", "Cryo Phantom", "Neural Wreck", "Starved God", "Black Sun", "Rotting Star"]

ARCHETYPES = [{"name": "Street Samurai", "desc": "Guerriero con codice"}, {"name": "Corporate Insider", "desc": "Ex-dipendente con segreti"}, {"name": "Black Market Dealer", "desc": "Specialista contrabbando"}, {"name": "Cybernetic Enforcer", "desc": "Braccio armato"}, {"name": "Data Thief", "desc": "Ladro di dati"}, {"name": "Pilot/Spacer", "desc": "Esperto di navi"}, {"name": "Underground Medic", "desc": "Medico clandestino"}, {"name": "Rebel Leader", "desc": "Visionario ribelle"}, {"name": "Corporate Assassin", "desc": "Killer professionista"}, {"name": "AI Whisperer", "desc": "Parla con le IA"}, {"name": "Void Cultist", "desc": "Adoratore del vuoto"}, {"name": "Cryo Survivor", "desc": "Sopravvissuto a ibernazione fallita"}, {"name": "Corporate Defector", "desc": "Fuggito dopo aver visto troppo"}, {"name": "Neural Wreck", "desc": "Ex-hacker con mente danneggiata"}, {"name": "Black Ops Veteran", "desc": "Ex-soldato di operazioni segrete"}, {"name": "Station Rat", "desc": "Sopravvissuto nelle stazioni abbandonate"}, {"name": "Synthetic Sympathizer", "desc": "Difensore dei diritti delle IA"}, {"name": "Plague Doctor", "desc": "Medico di quarantene estreme"}, {"name": "Asteroid Miner", "desc": "Lavoratore delle miniere profonde"}, {"name": "Ghost Protocol", "desc": "Agente fantasma di operazioni nere"}]

PERSONALITIES = [{"tratto": "Paranoid", "desc": "Diffida di tutti"}, {"tratto": "Ruthless", "desc": "Sacrifica chiunque"}, {"tratto": "Idealistic", "desc": "Crede in un futuro migliore"}, {"tratto": "Cynical", "desc": "Non si fida di nessuno"}, {"tratto": "Charismatic", "desc": "Attira follower"}, {"tratto": "Greedy", "desc": "Tutto ha un prezzo"}, {"tratto": "Curious", "desc": "Non resiste ai misteri"}, {"tratto": "Vengeful", "desc": "Ricorda ogni torto"}, {"tratto": "Playful", "desc": "Tratta la morte come gioco"}, {"tratto": "Stoic", "desc": "Emozioni = vulnerabilità"}, {"tratto": "Hollow", "desc": "Ha perso ogni emozione"}, {"tratto": "Fanatical", "desc": "Crede ciecamente in una causa"}, {"tratto": "Broken", "desc": "Sopravvissuto a traumi estremi"}, {"tratto": "Predatory", "desc": "Vede tutti come prede o predatori"}, {"tratto": "Resigned", "desc": "Ha accettato la fine"}, {"tratto": "Obsessive", "desc": "Fissato su un obiettivo"}, {"tratto": "Detached", "desc": "Osserva tutto con distacco"}, {"tratto": "Desperate", "desc": "Pronta a tutto per sopravvivere"}, {"tratto": "Nihilistic", "desc": "Nulla ha senso"}, {"tratto": "Zealous", "desc": "Convinta di avere una missione divina"}]

TRATTI_FISICI = ["Cicatrice che attraversa l’occhio sinistro", "Occhio destro completamente nero", "Tatuaggio che copre metà del viso", "Capelli rasati con disegni geometrici", "Protesi al posto di un orecchio", "Voce leggermente metallica", "Mani insolitamente grandi", "Pelle molto pallida o molto scura", "Occhi di due colori diversi", "Cicatrici multiple sul collo", "Denti affilati o dorati", "Andatura leggermente zoppicante", "Mani costantemente sporche di olio", "Sguardo molto intenso o vuoto", "Capelli lunghi e spettinati", "Pelle con venature luminose", "Voce molto bassa o molto acuta", "Braccio sinistro più muscoloso", "Cicatrice a forma di fulmine sul viso", "Occhi che cambiano leggermente colore", "Tatuaggi che coprono entrambe le braccia", "Postura rigida o eccessivamente rilassata", "Pelle con piccole cicatrici da ustione", "Dita insolitamente lunghe", "Sguardo che evita il contatto visivo", "Capelli tinti di colori innaturali", "Voce con leggero eco", "Braccio destro coperto da placche metalliche", "Pelle con macchie scure", "Andatura felina o aggressiva", "Cicatrice che divide le sopracciglia", "Mani sempre fredde", "Sguardo che sembra leggere dentro le persone", "Capelli molto corti o completamente rasati", "Voce rauca o roca", "Protesi visibile su una gamba", "Pelle con leggere luminescenze", "Espressione facciale quasi sempre neutra", "Mani con calli molto evidenti", "Sguardo che sorride anche quando la bocca no", "Pelle con vene nere pulsanti", "Occhio con pupilla dilatata permanentemente", "Cicatrice a forma di croce sul petto", "Protesi che emette suoni inquietanti", "Pelle con pattern di circuiti", "Voce che cambia tono casualmente", "Mani con unghie nere", "Sguardo che sembra guardare attraverso le persone", "Capelli che cadono a ciocche", "Pelle con macchie di sangue secco", "Voce che sembra provenire da più direzioni", "Andatura che sembra galleggiare"]

VESTIARIO = ["Tuta da pilota stealth", "Giacca con LED integrati", "Cappotto olografico retrattile", "Armatura leggera mimetica", "Tuta synthweave rinforzata", "Giubbotto con placche balistiche", "Cappuccio con visore notturno", "Tuta da lavoro intera", "Giacca con tasche multiple", "Abito elegante cyberpunk", "Tuta mimetica urbana", "Cappotto con cappuccio termico", "Giubbotto tattico modulare", "Tuta da combattimento leggera", "Abito con inserti luminosi", "Cappotto lungo con LED", "Tuta da tecnico con tasche", "Giacca con rinforzi metallici", "Tuta intera nera opaca", "Cappuccio con proiettore olografico", "Armatura leggera da campo", "Giacca con strisce riflettenti", "Tuta da pilota con patch", "Cappotto pesante termico", "Abito elegante sdrucito", "Tuta da quarantena con sigilli", "Giacca con sangue secco", "Cappotto con fori di proiettili", "Tuta da ibernazione strappata", "Armatura con segni di corrosione", "Cappuccio con maschera antigas", "Tuta da minatore con strati di polvere", "Giacca con patch di fazioni morte", "Cappotto con LED spenti", "Tuta da laboratorio con macchie chimiche", "Armatura da assalto danneggiata", "Cappuccio con visore crepato"]

VISIBLE_DAMAGE = ["Nessun danno evidente"] * 25 + ["Cicatrice da laser sottile", "Ustione chimica sul braccio", "Impianto guasto con scintille", "Cicatrice da proiettile", "Protesi danneggiata con cavi esposti", "Ustione da sovraccarico neurale", "Cicatrice da coltello vibro", "Impianto oculare crepato", "Pelle con vene nere", "Cicatrice da esplosione", "Protesi con placca arrugginita", "Tatuaggio bruciato", "Impianto spinale malfunzionante", "Cicatrice da morso di drone", "Pelle con macchie luminescenti", "Protesi con giuntura bloccata", "Cicatrice da frusta monofilamento", "Impianto con perdita di fluido", "Ustione da plasma", "Cicatrice da sparo ravvicinato", "Protesi con vernice scrostata", "Segni di graffi profondi", "Impianto con LED malfunzionanti", "Cicatrice da coltello termico", "Danno grave multiplo", "Pelle con vene nere pulsanti", "Occhio con pupilla dilatata permanentemente", "Cicatrice a forma di croce sul petto", "Protesi che perde fluido nero", "Pelle con pattern di circuiti bruciati", "Voce con eco metallico permanente", "Mani con unghie nere e rotte", "Sguardo con vene rosse permanenti", "Capelli con ciocche grigie improvvise", "Pelle con macchie di sangue secco", "Voce che sembra provenire da più direzioni", "Andatura che sembra galleggiare"]

ROLES = ["Hacker/Netrunner", "Smuggler", "Bounty Hunter", "Corporate Fixer", "Explorer/Scout", "Mercenary", "Cyberdoc", "Pilot/Spacer", "Technician/Engineer", "Data Broker", "Rebel/Insurgent", "Cultist/Mystic", "Trader/Merchant", "Security Officer", "Scientist/Researcher", "Assassin/Shadow Operative", "Diplomat/Negotiator", "Scavenger/Salvager", "AI Specialist/Synth Whisperer", "Debt Collector/Enforcer", "Support", "Navigator"]

SKILLS = {"PHYSICAL": ["Might", "Agility", "Endurance"], "TECH": ["Medicine", "Engineering"], "DIGITAL": ["Browsing", "Hacking"], "PILOT": ["Spaceship", "Vehicle"], "SURVIVAL": ["Senses", "Tracking"], "SOCIAL": ["Cunning", "Fear", "Mannerism"], "WEAPONS": ["Melee", "Explosives", "Ranged"], "LORE": ["Science", "History", "Investigation", "Linguistics"]}

ARMORS = [{"name": "Reinforced Clothing", "ap": 1}, {"name": "Armor Vest", "ap": 4}, {"name": "Standard Infantry Armor", "ap": 7}, {"name": "Powered Infantry Armor", "ap": 14}, {"name": "Subdermal Armor", "ap": 0}]

WEAPONS = [{"name": "Combat Knife", "dmg": "1d5+MDM"}, {"name": "Autopistol", "dmg": "1d10+1"}, {"name": "Revolver", "dmg": "1d10+3"}, {"name": "Hand Cannon", "dmg": "1d10+2"}, {"name": "Assault Rifle", "dmg": "2d10+2"}, {"name": "Pulse Rifle", "dmg": "3d10"}, {"name": "Pump Shotgun", "dmg": "3d10/1d10+3"}, {"name": "Sniper Rifle", "dmg": "3d10"}, {"name": "Flamethrower", "dmg": "2d10 (AA)"}]

DEVASTATING_WEAPONS = [{"name": "Railgun Sniper", "dmg": "4d10"}, {"name": "Smart Rifle", "dmg": "4d10"}, {"name": "Heavy Plasma Cannon", "dmg": "4d10"}]

TRINKETS = ["Ciondolo con foto sbiadita", "Accendino cromato consumato", "Chiave USB logora", "Collana con dente di drago", "Orologio rotto con data incisa", "Flacone di pillole vuote", "Piccolo drone rotto", "Carta da gioco con bordo dorato", "Flacone di profumo costoso", "Moneta antica con foro", "Piccolo coltello pieghevole", "Scheda di memoria con canzoni", "Anello con pietra nera", "Kit di riparazione per droni", "Lettera sigillata mai aperta", "Flacone di stimolanti", "Piccolo specchio incrinato", "Chiave di una vecchia astronave", "Pacchetto di sigarette elettroniche", "Piccolo libro di poesie cyberpunk", "Braccialetto con codice QR", "Flacone di lubrificante per protesi", "Dado a 20 facce consumato", "Piccolo flacone di acqua santa", "Scheda di accesso rubata", "Collana con dente di lupo", "Piccolo registratore vocale", "Flacone di crema rigenerante", "Chiave inglese antica", "Piccolo portafortuna a forma di sole", "Flacone di feromoni sintetici", "Piccolo libro di codici cifrati", "Braccialetto con luci LED", "Flacone di pillole per il sonno", "Piccolo coltello da lancio", "Scheda di memoria con foto di famiglia", "Flacone di lubrificante per armature", "Piccolo drone da compagnia (rotto)", "Lettera d'amore mai spedita", "Flacone di stimolanti da combattimento", "Piccolo specchio con incisione", "Chiave di un deposito segreto", "Flacone di profumo", "Piccolo libro di preghiere IA", "Braccialetto con sensore di salute", "Flacone di antidoto generico", "Piccolo coltello da combattimento", "Scheda di memoria con diario vocale", "Flacone di crema per cicatrici", "Piccolo drone da sorveglianza (rotto)", "Collana con croce di neon", "Flacone di stimolanti mentali", "Piccolo libro di ricette di strada", "Braccialetto con codice di accesso", "Flacone di lubrificante per protesi", "Piccolo coltello da combattimento bilanciato", "Scheda di memoria con mappe segrete", "Flacone di antidolorifici forti", "Piccolo drone da compagnia (funzionante)", "Lettera di dimissioni mai spedita", "Flacone di feromoni da combattimento", "Piccolo libro di codici morse", "Braccialetto con sensore di radiazioni", "Flacone di crema rigenerante avanzata", "Piccolo coltello da lancio bilanciato", "Scheda di memoria con registrazioni segrete", "Flacone di lubrificante per droni", "Piccolo libro di poesie perdute", "Braccialetto con luci di emergenza", "Flacone di antidoto specifico", "Piccolo drone da ricognizione (rotto)", "Lettera di addio mai letta", "Flacone di lubrificante per armature pesanti", "Piccolo coltello da sopravvivenza", "Scheda di memoria con mappe di Capital", "Flacone di stimolanti da hacking", "Piccolo libro di preghiere per IA", "Braccialetto con sensore di stress", "Flacone di crema per ustioni", "Piccolo drone da compagnia (avanzato)", "Lettera di ricatto mai spedita", "Flacone di stimolanti da combattimento avanzati", "Piccolo libro di codici antichi", "Braccialetto con luci di segnalazione", "Flacone di antidoto universale", "Piccolo coltello da combattimento bilanciato", "Scheda di memoria con diari di guerra", "Flacone di lubrificante per droni", "Piccolo libro di ricette di strada avanzate", "Braccialetto con sensore di radiazioni avanzato", "Flacone di crema rigenerante sperimentale", "Piccolo drone da sorveglianza avanzato", "Lettera di dimissioni firmata", "Flacone di stimolanti mentali avanzati", "Piccolo libro di codici di sicurezza", "Braccialetto con luci di emergenza avanzate", "Flacone di antidoto sperimentale", "Piccolo coltello da lancio bilanciato avanzato", "Scheda di memoria con registrazioni segrete avanzate", "Flacone di stimolanti da combattimento sperimentali"]

BACKGROUNDS = [{"name": "Ex-Corporate", "desc": "Ex-dipendente di una mega-corp", "bonus": "+2 LORE"}, {"name": "Street Rat", "desc": "Cresciuto nei bassifondi", "bonus": "+2 SURVIVAL"}, {"name": "Ex-Soldato", "desc": "Veterano di guerre corporative", "bonus": "+2 WEAPONS"}, {"name": "Underground Hacker", "desc": "Ex-membro di un collettivo hacker", "bonus": "+3 DIGITAL"}, {"name": "Scavenger Pro", "desc": "Professionista del recupero", "bonus": "+3 SURVIVAL"}, {"name": "Pilot Smuggler", "desc": "Trasportatore illegale", "bonus": "+3 PILOT"}, {"name": "Corporate Defector", "desc": "Fuggito da una mega-corp", "bonus": "+2 LORE + 1 SOCIAL"}, {"name": "Rebel Sympathizer", "desc": "Supporta un movimento ribelle", "bonus": "+2 SOCIAL"}, {"name": "Synth Whisperer", "desc": "Specialista nel trattare con IA", "bonus": "+3 LORE"}, {"name": "Black Market Fixer", "desc": "Mediatore del mercato nero", "bonus": "+3 SOCIAL"}, {"name": "Ex-Security Officer", "desc": "Ex-guardia di una Capital", "bonus": "+2 WEAPONS"}, {"name": "Street Doctor", "desc": "Medico senza licenza", "bonus": "+3 TECH (Medicine)"}, {"name": "Corporate Assassin (Ritirato)", "desc": "Ex-killer professionista", "bonus": "+3 WEAPONS"}, {"name": "Data Broker", "desc": "Venditore di informazioni", "bonus": "+3 DIGITAL"}, {"name": "Synth Companion", "desc": "Ex-compagno sintetico", "bonus": "+2 SOCIAL + 1 LORE"}, {"name": "Grid Rat", "desc": "Cresciuto in un Patch", "bonus": "+2 TECH + 1 SURVIVAL"}, {"name": "Ex-Cult Member", "desc": "Ex-membro di setta techno-religiosa", "bonus": "+2 LORE + 1 SOCIAL"}, {"name": "Debt Collector", "desc": "Ex-recuperatore di debiti", "bonus": "+2 SOCIAL + 1 WEAPONS"}, {"name": "Deep Spacer", "desc": "Ha passato anni nello spazio", "bonus": "+3 PILOT + 1 SURVIVAL"}, {"name": "Information Broker", "desc": "Specialista nel raccogliere segreti", "bonus": "+3 LORE"}]

ALLINEAMENTI = [{"name": "Corporate Loyalist", "desc": "Fedele alle mega-corporazioni"}, {"name": "Rebel Anarchist", "desc": "Vuole abbattere il sistema"}, {"name": "Neutral Scavenger", "desc": "Sopravvive a tutti i costi"}, {"name": "Lawful Enforcer", "desc": "Rispetta le regole del potere"}, {"name": "Chaotic Opportunist", "desc": "Fa quello che gli conviene"}, {"name": "Idealist Visionary", "desc": "Cerca un mondo migliore"}]

MEGACORPS = [{"name": "Aether Dynamics", "desc": "Dominano l'energia e lo spazio profondo", "type": "IN GRID"}, {"name": "Kronos Heavy Industries", "desc": "Armi, armature e infrastrutture pesanti", "type": "IN GRID"}, {"name": "Nexus Data Systems", "desc": "IA, dati e sorveglianza totale", "type": "IN GRID"}, {"name": "Vanguard Logistics", "desc": "Trasporti, contrabbando e rotte interstellari", "type": "EXTRA GRID"}, {"name": "Eclipse BioTech", "desc": "Cyberware, genetica e stimolanti", "type": "IN GRID"}, {"name": "Ironclad Security", "desc": "Forze paramilitari e sicurezza privata", "type": "IN GRID"}, {"name": "Helix Pharmaceuticals", "desc": "Farmaci, droghe e bio-potenziamenti", "type": "EXTRA GRID"}, {"name": "VoidForge Shipyards", "desc": "Costruzione di navi e stazioni spaziali", "type": "EXTRA GRID"}, {"name": "Spectra Entertainment", "desc": "Media, propaganda e intrattenimento di massa", "type": "IN GRID"}, {"name": "Titan Mining Conglomerate", "desc": "Estrazione di risorse su asteroidi e lune", "type": "EXTRA GRID"}]

DISPOSITIONS = {
    "+3 Protezione": {"desc": "L'NPC proteggerà attivamente il party.", "adjectives": ["Leale", "Protettivo", "Dedicato", "Fidato"]},
    "+2 Contatto": {"desc": "L'NPC è amichevole e collaborativo.", "adjectives": ["Amichevole", "Disponibile", "Aperto", "Cordiale"]},
    "+1 Neutralità": {"desc": "L'NPC è neutrale e pragmatico.", "adjectives": ["Neutrale", "Pragmatico", "Opportunista", "Calcolatore"]},
    "-1 Resilienza": {"desc": "L'NPC resisterà passivamente e sarà diffidente.", "adjectives": ["Diffidente", "Cauto", "Riservato", "Sospettoso"]},
    "-2 Ostacolo": {"desc": "L'NPC creerà ostacoli attivi.", "adjectives": ["Ostile", "Aggressivo", "Minaccioso", "Conflittuale"]},
    "-3 Ostilità Totale": {"desc": "L'NPC attaccherà attivamente il party.", "adjectives": ["Violento", "Pericoloso", "Assassino", "Spietato"]}
}

# ============================================================
#  FUNZIONI OTTIMIZZATE
# ============================================================

def get_random_faction():
    return random.choice(MEGACORPS)

def get_expanded_equipment(role, power, category):
    base = []
    if category == "Civilian": base = ["Toolkit professionale", "500 credits", "Documento d'identità falso"]
    elif category == "Combat": base = ["Medkit da campo", "Granate (2)", "Comunicatore criptato"]
    elif category == "Scum": base = ["Toolkit da infiltrazione", "Droga leggera (2 dosi)", "Contanti non tracciabili"]
    if power >= 10: base.append("Drone da ricognizione")
    if power >= 14: base.append("Neural Deck avanzato" if "Hacker" in role or "Data Broker" in role else "Armatura rinforzata")
    if power >= 17: base.append("Crediti offshore (2000cr)")
    role_equip = {"Hacker/Netrunner": ["Neural Deck", "Virus custom (3)", "Accesso backdoor"], "Mercenary": ["Fucile d'assalto", "Armatura tattica", "Stimpak (2)"], "Corporate Fixer": ["Tablet criptato", "Contatti influenti", "Bustarelle pronte"], "Pilot/Spacer": ["Navicomputer", "Vaccsuit rinforzato", "Licenza di volo falsa"], "Cyberdoc": ["Kit medico avanzato", "Cyberware di ricambio", "Stimolanti"], "Data Broker": ["Database rubati", "Contatti nel darkweb", "Criptovaluta"], "Assassin/Shadow Operative": ["Fucile di precisione", "Silenziatore", "Veleni"], "Scavenger/Salvager": ["Metal detector", "Drone da recupero", "Mappa di relitti"]}
    if role in role_equip: base.extend(role_equip[role])
    return list(set(base))

def generate_extra_equipment(role, power, category, max_items=6):
    extra_pool = []
    if category == "Civilian": extra_pool = ["Tablet criptato", "Contanti non tracciabili", "Documento falso", "Kit di riparazione", "Flacone di stimolanti", "Mappa di contatti", "Drone da compagnia", "Licenza falsa"]
    elif category == "Combat": extra_pool = ["Granate (3)", "Stimpak (4)", "Armatura rinforzata", "Fucile d'assalto", "Medkit da campo", "Comunicatore criptato", "Drone da ricognizione", "C4 (2 cariche)"]
    elif category == "Scum": extra_pool = ["Toolkit da infiltrazione", "Droga leggera (4 dosi)", "Contanti non tracciabili", "Chiave di un deposito", "Veleno (3 dosi)", "Silencer", "Drone da sorveglianza", "Mappa di contatti criminali"]
    if "Hacker" in role or "Data Broker" in role: extra_pool.extend(["Neural Deck", "Virus custom", "Accesso backdoor"])
    if "Pilot" in role: extra_pool.extend(["Navicomputer", "Vaccsuit rinforzato"])
    if "Cyberdoc" in role: extra_pool.extend(["Kit medico avanzato", "Cyberware di ricambio"])
    return random.sample(extra_pool, min(max_items, len(extra_pool)))

def generate_allies_adversaries():
    pool = NAMES + SURNAMES
    return random.sample(pool, min(3, len(pool))), random.sample(pool, min(3, len(pool)))

def get_disposition(level):
    return DISPOSITIONS.get(level, {"desc": "Disposizione casuale.", "adjectives": ["Imprevedibile"]})

def generate_npc(power_pref=None, role_pref=None):
    if power_pref and power_pref != "Casuale":
        power_ranges = {"Debole (1-6)": (1, 6), "Competente (6-12)": (6, 12), "Forte (12-18)": (12, 18), "Minaccia (18-20)": (18, 20)}
        low, high = power_ranges[power_pref]
        power = random.randint(low, high)
    else:
        power = random.randint(1, 20)

    category = role_pref if role_pref and role_pref != "Casuale" else random.choice(["Civilian", "Combat", "Scum", "Support", "Navigator"])
    is_android = random.random() < 0.07
    if is_android: category = "Android"

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

    max_stat = 95 if power >= 15 else 85
    strength = min(max_stat, 20 + sum(random.randint(1, 10) for _ in range(4)))
    speed = min(max_stat, 20 + sum(random.randint(1, 10) for _ in range(4)))
    intellect = min(max_stat, 20 + sum(random.randint(1, 10) for _ in range(4)))
    combat = min(max_stat, 20 + sum(random.randint(1, 10) for _ in range(4)))

    if "Mercenary" in role or "Assassin" in role: combat = min(max_stat, combat + 15)
    if "Hacker" in role or "Data Broker" in role: intellect = min(max_stat, intellect + 15)
    if "Pilot" in role or "Scavenger" in role: speed = min(max_stat, speed + 12)
    if "Cyberdoc" in role: intellect = min(max_stat, intellect + 10)

    sanity = 10 + sum(random.randint(1, 10) for _ in range(4))
    fear = 10 + sum(random.randint(1, 10) for _ in range(4))
    body_save = 10 + sum(random.randint(1, 10) for _ in range(4))

    body = min(max_stat, 35 + power * 2 + random.randint(-5, 8))
    speed_stat = min(max_stat, 35 + power * 2 + random.randint(-5, 8))
    intellect_stat = min(max_stat, 35 + power * 2 + random.randint(-5, 8))
    combat_stat = min(max_stat, 15 + power * 2)
    hits = 1 + (power // 5)

    # === NUOVO SISTEMA BONUS SKILL PER CATEGORIA ===
    bonus = 0
    if power <= 6: bonus = 0
    elif power <= 12: bonus = 10
    elif power <= 18: bonus = 15
    else: bonus = 20

    skills_str = [f"{cat[:3]}({sub[:3]}):+{min(max_stat, 20 + power * 2 + random.randint(-8, 12))}" for cat, subs in list(SKILLS.items())[:4] for sub in subs[:2]]

    # Applica bonus automatico
    if category == "Combat":
        skill_group = random.choice(["WEAPONS", "PHYSICAL"])
        sub = random.choice(SKILLS[skill_group])
        skills_str.append(f"{skill_group[:3]}({sub[:3]}):+{bonus}")
    elif category == "Scum":
        skill_group = random.choice(["LORE", "SOCIAL"])
        sub = random.choice(SKILLS[skill_group])
        skills_str.append(f"{skill_group[:3]}({sub[:3]}):+{bonus}")
    elif category == "Civilian":
        skill_group = random.choice(["TECH", "DIGITAL", "PILOT"])
        sub = random.choice(SKILLS[skill_group])
        skills_str.append(f"{skill_group[:3]}({sub[:3]}):+{bonus}")
    elif category == "Support":
        skill_group = random.choice(["TECH", "DIGITAL", "PHYSICAL"])
        sub = random.choice(SKILLS[skill_group])
        skills_str.append(f"{skill_group[:3]}({sub[:3]}):+{bonus}")
    elif category == "Navigator":
        skill_group = random.choice(["PILOT", "PHYSICAL", "SURVIVAL"])
        sub = random.choice(SKILLS[skill_group])
        skills_str.append(f"{skill_group[:3]}({sub[:3]}):+{bonus}")

    armor, weapon, extra = generate_equipment(role, power, background, category)
    trinket = random.choice(TRINKETS)
    vestiario = random.choice(VESTIARIO)

    android_note = " [ANDROIDE]" if is_android else ""

    output = f"""
**{full_name}** | {age} anni | {sex} ({pronouns}){android_note}  
**{category} / {role}** | **Potenza: {power}** | Allineamento: {allineamento['name']}

**Background**: {background['name']} — {background['desc']}  
**Bonus**: {background['bonus']}

**Visible Damage**: {visible_damage}  
**Debito**: {debt} ({debt_status})

**ATTRIBUTI**  
**Strength**: {strength} | **Speed**: {speed} | **Intellect**: {intellect} | **Combat**: {combat}

**SAVES**  
**Sanity**: {sanity} | **Fear**: {fear} | **Body**: {body_save}

**Hits**: {hits} | **Body**: {body} | **Speed**: {speed_stat} | **Intellect**: {intellect_stat} | **Combat**: +{combat_stat}

**Skills**: {', '.join(skills_str)}

**Tratti Fisici**: {', '.join(tratti_fisici)}  
**Vestiario**: {vestiario}

**EQUIPAGGIAMENTO**  
- **Armor**: {armor['name']} (AP {armor['ap']})  
- **Weapon**: {weapon['name']} ({weapon['dmg']} DMG)  
- **Extra**: {', '.join(extra) if extra else 'Nessun extra'}  
- **Trinket**: {trinket}

**Flavor**: {pers['desc']}. {arch['desc']}.
"""
    return output, full_name, power, category

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
    return armor, weapon, extra

# ============================================================
#  INTERFACCIA OTTIMIZZATA
# ============================================================

st.title("🪐 Mothership NPC Generator v5.6 - OTTIMIZZATA")
st.markdown("**Versione pulita e ottimizzata** — Tutti gli elementi + Equipaggiamento Extra + Alleati/Avversari + Disposizione")

with st.sidebar:
    st.header("⚙️ Impostazioni")
    power_option = st.selectbox("Range Potenza", ["Casuale", "Debole (1-6)", "Competente (6-12)", "Forte (12-18)", "Minaccia (18-20)"])
    role_option = st.selectbox("Preferenza Ruolo", ["Casuale", "Civilian", "Combat", "Scum", "Support", "Navigator"])
    num_npcs = st.slider("Numero di NPC da generare", 1, 8, 1)

    st.markdown("---")
    st.subheader("Opzioni Avanzate")
    add_extra_equip = st.checkbox("Equipaggiamento Extra (fino a 6)", value=True)
    generate_allies = st.checkbox("Alleati e Avversari", value=True)
    disposition_level = st.selectbox("Disposizione Iniziale", ["Casuale"] + list(DISPOSITIONS.keys()))

if st.button("🚀 GENERA NPC", type="primary", use_container_width=True):
    for i in range(num_npcs):
        npc_text, name, power, cat = generate_npc(power_option, role_option)
        faction = get_random_faction()
        expanded_equip = get_expanded_equipment(role_option if role_option != "Casuale" else random.choice(ROLES), power, cat)
        
        extra_equip = generate_extra_equipment(role_option if role_option != "Casuale" else random.choice(ROLES), power, cat) if add_extra_equip else []
        allies, adversaries = generate_allies_adversaries() if generate_allies else ([], [])
        disposition = get_disposition(disposition_level) if disposition_level != "Casuale" else {"desc": "Disposizione casuale.", "adjectives": ["Imprevedibile"]}
        
        with st.expander(f"**{name}** — Potenza {power} | {cat}", expanded=(i == 0)):
            st.markdown(npc_text)
            st.markdown("---")
            
            st.markdown(f"**🏢 Affiliazione**: **{faction['name']}** ({faction['type']})")
            st.caption(faction['desc'])
            
            st.markdown(f"**🎒 Equipaggiamento Espanso**: {', '.join(expanded_equip)}")
            if extra_equip:
                st.markdown(f"**➕ Equipaggiamento Extra**: {', '.join(extra_equip)}")
            
            if generate_allies:
                st.markdown(f"**🤝 Alleati**: {', '.join(allies) if allies else 'Nessun alleato'}")
                st.markdown(f"**⚔️ Avversari**: {', '.join(adversaries) if adversaries else 'Nessun avversario'}")
            
            st.markdown(f"**🧭 Disposizione**: **{disposition_level}**")
            st.caption(disposition['desc'])
            st.caption(f"Aggettivi: {', '.join(disposition['adjectives'])}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.button("📋 Copia", key=f"copy_{i}")
            with col2:
                st.download_button("💾 .txt", npc_text, f"{name.replace(' ', '_')}.txt", key=f"dl_{i}")
            with col3:
                st.download_button("📄 .md", npc_text, f"{name.replace(' ', '_')}.md", key=f"dlmd_{i}")

st.markdown("---")
st.caption("Mothership NPC Generator v5.6 • Ottimizzato e pulito")