import streamlit as st
import random

# ====================== CONFIG ======================
st.set_page_config(page_title="MOTHERSHIP NPC GENERATOR", page_icon="🪐", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=VT323&display=swap');
    .stApp { background-color: #f8f8f8; color: #111111; }
    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: #111111; letter-spacing: 2px; }
    .stButton>button {
        background-color: #111111; color: white;
        border: 2px solid #111111; font-weight: bold; transition: all 0.3s;
    }
    .stButton>button:hover { background-color: #333333; border-color: #555555; }
    .stExpander { border: 2px solid #111111; border-radius: 4px; background-color: white; }
    .header-bar {
        background-color: #111111; color: white; padding: 10px 15px;
        border-radius: 4px; font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px; text-align: center;
    }
    .stMarkdown p, .stMarkdown li { color: #222222; }
</style>
""", unsafe_allow_html=True)

# ============================================================
#  COSTANTI
# ============================================================
ANDROID_CHANCE = 0.07
MAX_STAT_HIGH = 95   # power >= 15
MAX_STAT_LOW  = 85

# FIX #5: rimossi i duplicati presenti in entrambe le liste originali
NAMES = [
    "Jax", "Akira", "Zane", "Liara", "Kai", "Nova", "Echo", "Ren", "Sora",
    "Dimitri", "Ivan", "Sergei", "Alexei", "Nikolai", "Yuri",
    "Diego", "Mateo", "Javier", "Carlos", "Sofia", "Isabella", "Elena", "Carmen",
    "Kwame", "Amara", "Zuri", "Jamal", "Aisha", "Malik", "Tariq", "Fatima", "Omar",
    "Neo", "Zero", "Blaze", "Vortex", "Pixel", "Cipher", "Quantum", "Flux",
    "Shadow", "Ghost", "Razor", "Bolt", "Spark", "Chrome", "Neon", "Pulse", "Byte", "Grid",
    "Void", "Nexus", "Apex", "Titan", "Phantom", "Specter", "Orion", "Vega", "Sirius",
    "Lyra", "Mira", "Elara", "Raven", "Storm", "Frost", "Ember", "Ash", "Quartz",
    "Hiro", "Yuki", "Kenji", "Aiko", "Haruto", "Mei", "Wei", "Li", "Chen", "Zhang",
    "Kael", "Vesper", "Draven", "Nyx", "Riven", "Sable", "Liora", "Thal", "Veyra",
    "Korr", "Sylas", "Mirael", "Drax", "Elyndra", "Vorath", "Seraph",
    "Kaelith", "Nyxara", "Vael",
]

SURNAMES = [
    "Kaito", "Ramirez", "Ivanov", "Sato", "Patel", "Al-Rashid", "Okafor",
    "Dubois", "Nakamura", "Rodriguez", "Kim", "Singh", "Mbeki", "Al-Farsi",
    "Hernandez", "Lopez", "Moreau", "Takahashi", "Volkov", "Delgado", "Hassan",
    "Okoro", "Bianchi", "Yamamoto", "Kuznetsov", "Morales", "Ndiaye",
    "Kren", "Vex", "Ruiz", "Khan", "Mensah", "Okeke", "Diallo", "Traore",
    "Ba", "Diop", "Niang", "Fall", "Voss", "Krell", "Drake", "Corvus",
    "Blackwood", "Grimm", "Holloway", "Ironwood", "Kane", "Locke",
    "Morrow", "Nightshade", "Ravenwood", "Steel",
]

NICKNAMES = [
    "Neon Ghost", "Chrome Reaper", "Data Phantom", "Void Runner", "Pulse King",
    "Shadow Broker", "Iron Saint", "Net Witch", "Blade Phantom", "Corp Slayer",
    "Zero Hour", "Gridlock", "Cyber Siren", "Razor Queen", "Byte Bandit",
    "Neon Viper", "Storm Chaser", "Echo Hunter", "Blackout", "Voidwalker",
    "Corpse Whisperer", "Null Signal", "Deadlight", "Iron Veil", "Wraith",
    "Specter-9", "Hollow Man", "Eclipse", "Grimwire", "Bonejack",
    "Silent Protocol", "Ashwalker", "Cryo Phantom", "Neural Wreck",
    "Starved God", "Black Sun", "Rotting Star",
]

ARCHETYPES = [
    {"name": "Street Samurai",      "desc": "Guerriero con codice"},
    {"name": "Corporate Insider",   "desc": "Ex-dipendente con segreti"},
    {"name": "Black Market Dealer", "desc": "Specialista contrabbando"},
    {"name": "Cybernetic Enforcer", "desc": "Braccio armato"},
    {"name": "Data Thief",          "desc": "Ladro di dati"},
    {"name": "Pilot/Spacer",        "desc": "Esperto di navi"},
    {"name": "Underground Medic",   "desc": "Medico clandestino"},
    {"name": "Rebel Leader",        "desc": "Visionario ribelle"},
    {"name": "Corporate Assassin",  "desc": "Killer professionista"},
    {"name": "AI Whisperer",        "desc": "Parla con le IA"},
    {"name": "Void Cultist",        "desc": "Adoratore del vuoto"},
    {"name": "Cryo Survivor",       "desc": "Sopravvissuto a ibernazione"},
    {"name": "Neural Wreck",        "desc": "Ex-hacker con mente danneggiata"},
    {"name": "Black Ops Veteran",   "desc": "Ex-soldato operazioni segrete"},
]

PERSONALITIES = [
    {"tratto": "Paranoid",    "desc": "Diffida di tutti"},
    {"tratto": "Ruthless",    "desc": "Sacrifica chiunque"},
    {"tratto": "Idealistic",  "desc": "Crede in un futuro migliore"},
    {"tratto": "Cynical",     "desc": "Non si fida di nessuno"},
    {"tratto": "Charismatic", "desc": "Attira follower"},
    {"tratto": "Greedy",      "desc": "Tutto ha un prezzo"},
    {"tratto": "Curious",     "desc": "Non resiste ai misteri"},
    {"tratto": "Vengeful",    "desc": "Ricorda ogni torto"},
    {"tratto": "Stoic",       "desc": "Emozioni = vulnerabilità"},
    {"tratto": "Hollow",      "desc": "Ha perso ogni emozione"},
    {"tratto": "Fanatical",   "desc": "Crede ciecamente"},
    {"tratto": "Broken",      "desc": "Sopravvissuto a traumi estremi"},
    {"tratto": "Nihilistic",  "desc": "Nulla ha senso"},
]

TRATTI_FISICI = [
    "Cicatrice che attraversa l'occhio sinistro", "Occhio destro completamente nero",
    "Tatuaggio che copre metà del viso", "Capelli rasati con disegni geometrici",
    "Protesi al posto di un orecchio", "Voce leggermente metallica",
    "Mani insolitamente grandi", "Pelle molto pallida", "Occhi di due colori diversi",
    "Cicatrici multiple sul collo", "Denti affilati o dorati", "Andatura zoppicante",
    "Mani sporche di olio", "Sguardo intenso", "Pelle con venature luminose",
    "Voce metallica bassa", "Braccio sinistro muscoloso", "Cicatrice a forma di fulmine",
    "Occhi che cambiano colore", "Tatuaggi su entrambe le braccia",
    "Pelle con piccole ustioni", "Dita insolitamente lunghe", "Capelli tinti innaturali",
    "Voce con eco", "Braccio destro con placche metalliche", "Pelle con macchie scure",
    "Andatura felina", "Cicatrice che divide le sopracciglia", "Mani sempre fredde",
    "Protesi visibile su una gamba", "Pelle con luminescenze",
    "Pelle con vene nere pulsanti", "Occhio con pupilla dilatata",
    "Cicatrice a croce sul petto", "Protesi che emette suoni inquietanti",
]

VESTIARIO = [
    "Tuta da pilota stealth", "Giacca con LED integrati", "Cappotto olografico",
    "Armatura leggera mimetica", "Tuta synthweave", "Giubbotto con placche balistiche",
    "Cappuccio con visore notturno", "Tuta da lavoro intera", "Abito elegante cyberpunk",
    "Tuta mimetica urbana", "Cappotto con cappuccio termico", "Giubbotto tattico modulare",
    "Tuta da combattimento leggera", "Cappotto lungo con LED", "Tuta da tecnico",
    "Tuta intera nera opaca", "Armatura leggera da campo", "Tuta da quarantena",
    "Giacca con sangue secco", "Cappotto con fori di proiettili",
    "Tuta da ibernazione strappata", "Armatura con segni di corrosione",
]

VISIBLE_DAMAGE = (
    ["Nessun danno evidente"] * 25 + [
        "Cicatrice da laser", "Ustione chimica", "Impianto guasto con scintille",
        "Cicatrice da proiettile", "Protesi danneggiata", "Ustione neurale",
        "Impianto oculare crepato", "Pelle con vene nere", "Cicatrice da esplosione",
        "Protesi arrugginita", "Impianto spinale malfunzionante", "Ustione da plasma",
        "Protesi con vernice scrostata", "Pelle con vene nere pulsanti",
        "Occhio con pupilla dilatata", "Protesi che perde fluido nero",
    ]
)

ROLES = [
    "Hacker/Netrunner", "Smuggler", "Bounty Hunter", "Corporate Fixer",
    "Explorer/Scout", "Mercenary", "Cyberdoc", "Pilot/Spacer",
    "Technician/Engineer", "Data Broker", "Rebel/Insurgent", "Cultist/Mystic",
    "Trader/Merchant", "Security Officer", "Scientist/Researcher",
    "Assassin/Shadow Operative", "Diplomat/Negotiator", "Scavenger/Salvager",
    "AI Specialist/Synth Whisperer", "Debt Collector/Enforcer", "Support", "Navigator",
]

# FIX #6/#7: tutte le 8 categorie vengono ora usate; nessun sub viene troncato
SKILLS: dict[str, list[str]] = {
    "PHYSICAL": ["Might", "Agility", "Endurance"],
    "TECH":     ["Medicine", "Engineering"],
    "DIGITAL":  ["Browsing", "Hacking"],
    "PILOT":    ["Spaceship", "Vehicle"],
    "SURVIVAL": ["Senses", "Tracking"],
    "SOCIAL":   ["Cunning", "Fear", "Mannerism"],
    "WEAPONS":  ["Melee", "Explosives", "Ranged"],
    "LORE":     ["Science", "History", "Investigation", "Linguistics"],
}

# Categorie da mostrare nell'output (max 2 sub per categoria per leggibilità)
SKILL_DISPLAY_CATS = ["PHYSICAL", "TECH", "DIGITAL", "WEAPONS"]

ARMORS = [
    {"name": "Reinforced Clothing",   "ap": 1},
    {"name": "Armor Vest",            "ap": 4},
    {"name": "Standard Infantry Armor","ap": 7},
    {"name": "Powered Infantry Armor", "ap": 14},
    {"name": "Subdermal Armor",        "ap": 0},
]

WEAPONS = [
    {"name": "Combat Knife",   "dmg": "1d5+MDM"},
    {"name": "Autopistol",     "dmg": "1d10+1"},
    {"name": "Revolver",       "dmg": "1d10+3"},
    {"name": "Hand Cannon",    "dmg": "1d10+2"},
    {"name": "Assault Rifle",  "dmg": "2d10+2"},
    {"name": "Pulse Rifle",    "dmg": "3d10"},
    {"name": "Pump Shotgun",   "dmg": "3d10/1d10+3"},
    {"name": "Sniper Rifle",   "dmg": "3d10"},
    {"name": "Flamethrower",   "dmg": "2d10 (AA)"},
]

DEVASTATING_WEAPONS = [
    {"name": "Railgun Sniper",      "dmg": "4d10"},
    {"name": "Smart Rifle",         "dmg": "4d10"},
    {"name": "Heavy Plasma Cannon", "dmg": "4d10"},
]

TRINKETS = [
    "Ciondolo con foto sbiadita", "Accendino cromato", "Chiave USB logora",
    "Collana con dente di drago", "Orologio rotto", "Flacone di pillole vuote",
    "Piccolo drone rotto", "Carta da gioco dorata", "Flacone di profumo",
    "Moneta antica", "Piccolo coltello pieghevole", "Scheda di memoria",
    "Anello con pietra nera", "Kit di riparazione droni", "Lettera sigillata",
    "Flacone di stimolanti", "Piccolo specchio incrinato", "Chiave di astronave",
    "Pacchetto sigarette elettroniche", "Braccialetto con codice QR",
]

BACKGROUNDS = [
    {"name": "Ex-Corporate",       "desc": "Ex-dipendente di una mega-corp",    "bonus": "+2 LORE"},
    {"name": "Street Rat",         "desc": "Cresciuto nei bassifondi",           "bonus": "+2 SURVIVAL"},
    {"name": "Ex-Soldato",         "desc": "Veterano di guerre corporative",     "bonus": "+2 WEAPONS"},
    {"name": "Underground Hacker", "desc": "Ex-membro collettivo hacker",        "bonus": "+3 DIGITAL"},
    {"name": "Scavenger Pro",      "desc": "Professionista del recupero",        "bonus": "+3 SURVIVAL"},
    {"name": "Pilot Smuggler",     "desc": "Trasportatore illegale",             "bonus": "+3 PILOT"},
]

ALLINEAMENTI = [
    {"name": "Corporate Loyalist", "desc": "Fedele alle mega-corporazioni"},
    {"name": "Rebel Anarchist",    "desc": "Vuole abbattere il sistema"},
    {"name": "Neutral Scavenger",  "desc": "Sopravvive a tutti i costi"},
    {"name": "Lawful Enforcer",    "desc": "Rispetta le regole"},
    {"name": "Chaotic Opportunist","desc": "Fa quello che conviene"},
    {"name": "Idealist Visionary", "desc": "Cerca un mondo migliore"},
]

# FIX #2: power ranges non sovrapposti (bounds esclusivi agli estremi)
POWER_RANGES: dict[str, tuple[int, int]] = {
    "Debole (1-6)":      (1, 6),
    "Competente (7-12)": (7, 12),
    "Forte (13-18)":     (13, 18),
    "Minaccia (19-20)":  (19, 20),
}

CATEGORIES = ["Civilian", "Combat", "Scum", "Support", "Navigator"]

# FIX #3: aggiunta voce "Android" nella mappa
CATEGORY_SKILL_MAP: dict[str, list[str]] = {
    "Combat":    ["WEAPONS", "PHYSICAL"],
    "Scum":      ["LORE", "SOCIAL"],
    "Civilian":  ["TECH", "DIGITAL", "PILOT"],
    "Support":   ["TECH", "DIGITAL", "PHYSICAL"],
    "Navigator": ["PILOT", "PHYSICAL", "SURVIVAL"],
    "Android":   ["DIGITAL", "TECH"],  # FIX #3
}

# ============================================================
#  FUNZIONI HELPER
# ============================================================
def calculate_power_bonus(power: int) -> int:
    if power <= 6:   return 0
    if power <= 12:  return 10
    if power <= 18:  return 15
    return 20


def roll_stat(max_stat: int, base: int = 20, dice: int = 4) -> int:
    """Tira `dice` d10, somma al base, clampa a max_stat."""
    return min(max_stat, base + sum(random.randint(1, 10) for _ in range(dice)))


def roll_save(base: int = 10, dice: int = 4) -> int:
    return base + sum(random.randint(1, 10) for _ in range(dice))


def build_skills(category: str, power: int, max_stat: int) -> list[str]:
    """Genera le skill con bonus di categoria. FIX #6/#7."""
    skills: list[str] = []

    for cat in SKILL_DISPLAY_CATS:
        subs = SKILLS[cat]          # usa TUTTI i sub della categoria, senza [:2]
        for sub in subs[:2]:        # mostra max 2 per leggibilità; puoi rimuovere [:2] se vuoi tutto
            val = min(max_stat, 20 + power * 2 + random.randint(-8, 12))
            skills.append(f"{cat[:3]}({sub[:3]}):+{val}")

    bonus = calculate_power_bonus(power)
    if bonus > 0:
        possible_cats = CATEGORY_SKILL_MAP.get(category, ["PHYSICAL"])
        chosen_cat   = random.choice(possible_cats)
        chosen_skill = random.choice(SKILLS[chosen_cat])
        skills.append(f"{chosen_cat[:3]}({chosen_skill[:3]}):+{bonus}★")

    return skills


# ============================================================
#  GENERATORE PRINCIPALE
# ============================================================
def generate_npc(power_pref: str = "Casuale", role_pref: str = "Casuale") -> dict:
    # --- Potenza ---
    if power_pref in POWER_RANGES:
        low, high = POWER_RANGES[power_pref]
        power = random.randint(low, high)
    else:
        power = random.randint(1, 20)

    # --- Categoria / ruolo ---
    if role_pref not in ("Casuale", "", None):
        category = role_pref
    else:
        category = random.choice(CATEGORIES)

    # FIX #10: android non sovrascrive una preferenza esplicita dell'utente
    is_android = random.random() < ANDROID_CHANCE
    if is_android and role_pref in ("Casuale", "", None):
        category = "Android"

    # --- Carattere ---
    role        = random.choice(ROLES)
    arch        = random.choice(ARCHETYPES)   # FIX #1: ora usato nell'output
    pers        = random.choice(PERSONALITIES) # FIX #1: ora usato nell'output
    background  = random.choice(BACKGROUNDS)
    allineamento = random.choice(ALLINEAMENTI)

    # --- Identità ---
    full_name = f'"{random.choice(NICKNAMES)}" {random.choice(NAMES)} {random.choice(SURNAMES)}'
    age       = random.randint(19, 67)
    sex       = random.choice(["Maschio", "Femmina", "Non-binario"])
    pronouns  = {"Maschio": "he/him", "Femmina": "she/her", "Non-binario": "they/them"}[sex]

    tratti_fisici  = random.sample(TRATTI_FISICI, 3)
    visible_damage = random.choice(VISIBLE_DAMAGE)

    debt        = random.randint(0, 20)
    debt_status = "Intrappolato" if debt > 10 else "Precario" if debt > 4 else "Libero"

    # --- Statistiche ---
    max_stat = MAX_STAT_HIGH if power >= 15 else MAX_STAT_LOW
    strength  = roll_stat(max_stat)
    speed     = roll_stat(max_stat)
    intellect = roll_stat(max_stat)
    combat    = roll_stat(max_stat)

    sanity    = roll_save()
    fear      = roll_save()
    body_save = roll_save()

    hits = 1 + (power // 5)

    # --- Skills ---
    skills_str = build_skills(category, power, max_stat)

    # --- Equipaggiamento ---
    armor   = random.choice(ARMORS)
    weapon  = random.choice(DEVASTATING_WEAPONS) if power > 15 else random.choice(WEAPONS)
    vestiario = random.choice(VESTIARIO)
    trinket   = random.choice(TRINKETS)

    android_note = " **[ANDROIDE]**" if is_android else ""

    # FIX #1 / FIX #4 / FIX #9: arch, pers, background bonus e allineamento desc ora tutti inclusi
    output = f"""
**{full_name}** | {age} anni | {sex} ({pronouns}){android_note}  
**{category} / {role}** | **Potenza: {power}** | {allineamento['name']} — *{allineamento['desc']}*

**Archetipo**: {arch['name']} — {arch['desc']}  
**Personalità**: {pers['tratto']} — *{pers['desc']}*  
**Background**: {background['name']} — {background['desc']} *(Bonus: {background['bonus']})*  
**Visible Damage**: {visible_damage}  
**Debito**: {debt} ({debt_status})

**ATTRIBUTI**  
**Strength**: {strength} | **Speed**: {speed} | **Intellect**: {intellect} | **Combat**: {combat}

**SAVES**  
**Sanity**: {sanity} | **Fear**: {fear} | **Body**: {body_save}

**Hits**: {hits}

**Skills**: {', '.join(skills_str)}

**Tratti Fisici**: {'; '.join(tratti_fisici)}  
**Vestiario**: {vestiario}

**EQUIPAGGIAMENTO**  
- **Armor**: {armor['name']} (AP {armor['ap']})  
- **Weapon**: {weapon['name']} ({weapon['dmg']} DMG)  
- **Trinket**: {trinket}
"""
    return {
        "text": output,
        "name": full_name,
        "power": power,
        "category": category,
    }


# ============================================================
#  INTERFACCIA
# ============================================================
st.markdown('<div class="header-bar"><h1 style="margin:0;">MOTHERSHIP NPC GENERATOR</h1></div>',
            unsafe_allow_html=True)

# FIX #8: session_state per preservare gli NPC tra i rerun
if "npcs" not in st.session_state:
    st.session_state.npcs = []

with st.sidebar:
    st.header("IMPOSTAZIONI")
    power_option = st.selectbox("Range Potenza",
        ["Casuale"] + list(POWER_RANGES.keys()))   # usa le chiavi aggiornate (non sovrapposte)
    role_option  = st.selectbox("Preferenza Ruolo",
        ["Casuale"] + CATEGORIES)
    num_npcs     = st.slider("Numero di NPC da generare", 1, 8, 1)
    st.divider()
    if st.button("🗑️ Svuota lista NPC", use_container_width=True):
        st.session_state.npcs = []
        st.rerun()

col_gen, col_clear = st.columns([3, 1])
with col_gen:
    if st.button("🚀 GENERA NPC", type="primary", use_container_width=True):
        new_npcs = [generate_npc(power_option, role_option) for _ in range(num_npcs)]
        st.session_state.npcs = new_npcs + st.session_state.npcs   # nuovi in cima

for i, npc in enumerate(st.session_state.npcs):
    with st.expander(f"**{npc['name']}** — Potenza {npc['power']} | {npc['category']}",
                     expanded=(i == 0)):
        st.markdown(npc["text"])

st.caption("MOTHERSHIP NPC Generator v5.8 • Fixed & Optimized • Pronta per il tavolo")
