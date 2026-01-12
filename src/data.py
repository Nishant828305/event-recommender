# ---- RAW DATA ----
past_events_by_type = {
    "birthday": [
        {"location":"Delhi","guests":363,"venue":"Royal Hall","caterer":"Aman Caterers","decoration":"Luxury","cost":92839,"rating":4.6},
        {"location":"Bangalore","guests":88,"venue":"Green Lawn","caterer":"Urban Foods","decoration":"Basic","cost":457872,"rating":4.2},
        {"location":"Kolkata","guests":133,"venue":"City Banquet","caterer":"Aman Caterers","decoration":"Luxury","cost":270461,"rating":4.5},
        {"location":"Patna","guests":160,"venue":"City Banquet","caterer":"Aman Caterers","decoration":"Basic","cost":475998,"rating":4.7},
        {"location":"Ranchi","guests":92,"venue":"City Banquet","caterer":"Sharma Caterers","decoration":"Basic","cost":196214,"rating":4.4},
        {"location":"Bangalore","guests":443,"venue":"Royal Hall","caterer":"Royal Foods","decoration":"Theme","cost":229270,"rating":4.8},
        {"location":"Dhanbad","guests":477,"venue":"Grand Palace","caterer":"Royal Foods","decoration":"Minimal","cost":92485,"rating":4.8},
        {"location":"Dhanbad","guests":99,"venue":"Metro Hall","caterer":"Sharma Caterers","decoration":"Minimal","cost":82916,"rating":4.7},
        {"location":"Kolkata","guests":223,"venue":"Grand Palace","caterer":"Royal Foods","decoration":"Premium","cost":62778,"rating":4.5},
        {"location":"Dhanbad","guests":306,"venue":"Metro Hall","caterer":"Urban Foods","decoration":"Minimal","cost":368238,"rating":4.1},
        {"location":"Bangalore","guests":395,"venue":"City Banquet","caterer":"Royal Foods","decoration":"Theme","cost":450125,"rating":4.1},
    ],

    "wedding": [
        {"location":"Kolkata","guests":197,"venue":"Metro Hall","caterer":"Urban Foods","decoration":"Minimal","cost":158337,"rating":4.7},
        {"location":"Bangalore","guests":344,"venue":"Royal Hall","caterer":"Royal Foods","decoration":"Theme","cost":489670,"rating":4.6},
        {"location":"Patna","guests":474,"venue":"Green Lawn","caterer":"Royal Foods","decoration":"Premium","cost":77578,"rating":4.1},
        {"location":"Ranchi","guests":399,"venue":"City Banquet","caterer":"Urban Foods","decoration":"Premium","cost":155528,"rating":4.3},
        {"location":"Patna","guests":489,"venue":"Green Lawn","caterer":"Aman Caterers","decoration":"Premium","cost":65177,"rating":4.6},
        {"location":"Ranchi","guests":487,"venue":"Metro Hall","caterer":"Urban Foods","decoration":"Luxury","cost":421200,"rating":4.1},
        {"location":"Dhanbad","guests":245,"venue":"Green Lawn","caterer":"Sharma Caterers","decoration":"Premium","cost":410252,"rating":4.6},
        {"location":"Dhanbad","guests":227,"venue":"Metro Hall","caterer":"Aman Caterers","decoration":"Luxury","cost":167956,"rating":4.2},
    ],

    "anniversary": [
        {"location":"Kolkata","guests":452,"venue":"Grand Palace","caterer":"Sharma Caterers","decoration":"Luxury","cost":226636,"rating":4.5},
        {"location":"Patna","guests":189,"venue":"Royal Hall","caterer":"Royal Foods","decoration":"Theme","cost":302694,"rating":4.2},
        {"location":"Ranchi","guests":80,"venue":"Metro Hall","caterer":"Urban Foods","decoration":"Theme","cost":137057,"rating":4.1},
        {"location":"Patna","guests":220,"venue":"City Banquet","caterer":"Royal Foods","decoration":"Minimal","cost":331363,"rating":4.8},
        {"location":"Bangalore","guests":327,"venue":"Grand Palace","caterer":"Royal Foods","decoration":"Minimal","cost":84872,"rating":4.8},
        {"location":"Kolkata","guests":97,"venue":"Green Lawn","caterer":"Urban Foods","decoration":"Theme","cost":124019,"rating":4.1},
        {"location":"Dhanbad","guests":363,"venue":"Metro Hall","caterer":"Sharma Caterers","decoration":"Luxury","cost":209580,"rating":4.1},
        {"location":"Delhi","guests":451,"venue":"Royal Hall","caterer":"Aman Caterers","decoration":"Luxury","cost":199935,"rating":4.5},
        {"location":"Patna","guests":251,"venue":"Green Lawn","caterer":"Aman Caterers","decoration":"Premium","cost":207766,"rating":4.1},
    ],

    "seminar": [
        {"location":"Dhanbad","guests":428,"venue":"City Banquet","caterer":"Urban Foods","decoration":"Theme","cost":462063,"rating":4.8},
        {"location":"Delhi","guests":276,"venue":"City Banquet","caterer":"Sharma Caterers","decoration":"Minimal","cost":494111,"rating":4.5},
        {"location":"Kolkata","guests":395,"venue":"Grand Palace","caterer":"Aman Caterers","decoration":"Basic","cost":139638,"rating":4.0},
        {"location":"Bangalore","guests":415,"venue":"Royal Hall","caterer":"Sharma Caterers","decoration":"Minimal","cost":398561,"rating":4.3},
        {"location":"Kolkata","guests":128,"venue":"Metro Hall","caterer":"Urban Foods","decoration":"Basic","cost":390718,"rating":4.8},
        {"location":"Delhi","guests":99,"venue":"Grand Palace","caterer":"Royal Foods","decoration":"Basic","cost":334745,"rating":4.1},
        {"location":"Ranchi","guests":259,"venue":"Royal Hall","caterer":"Royal Foods","decoration":"Minimal","cost":421980,"rating":4.5},
    ],

    "festival": [
        {"location":"Patna","guests":175,"venue":"Metro Hall","caterer":"Aman Caterers","decoration":"Luxury","cost":338879,"rating":4.7},
        {"location":"Bangalore","guests":463,"venue":"Grand Palace","caterer":"Royal Foods","decoration":"Basic","cost":43075,"rating":4.3},
        {"location":"Dhanbad","guests":134,"venue":"Metro Hall","caterer":"Aman Caterers","decoration":"Minimal","cost":266391,"rating":4.4},
        {"location":"Ranchi","guests":199,"venue":"Green Lawn","caterer":"Aman Caterers","decoration":"Minimal","cost":62767,"rating":4.9},
        {"location":"Delhi","guests":437,"venue":"Metro Hall","caterer":"Urban Foods","decoration":"Luxury","cost":474871,"rating":4.3},
        {"location":"Bangalore","guests":203,"venue":"Royal Hall","caterer":"Royal Foods","decoration":"Minimal","cost":356444,"rating":4.6},
        {"location":"Delhi","guests":130,"venue":"Royal Hall","caterer":"Sharma Caterers","decoration":"Basic","cost":487820,"rating":4.2},
        {"location":"Dhanbad","guests":428,"venue":"Green Lawn","caterer":"Urban Foods","decoration":"Minimal","cost":394309,"rating":4.1},
        {"location":"Ranchi","guests":334,"venue":"Metro Hall","caterer":"Aman Caterers","decoration":"Luxury","cost":282504,"rating":4.2},
        {"location":"Ranchi","guests":81,"venue":"Metro Hall","caterer":"Sharma Caterers","decoration":"Theme","cost":47682,"rating":4.5},
    ],

    "corporate": [
        {"location":"Patna","guests":71,"venue":"Green Lawn","caterer":"Royal Foods","decoration":"Premium","cost":435077,"rating":4.4},
        {"location":"Ranchi","guests":462,"venue":"Green Lawn","caterer":"Aman Caterers","decoration":"Premium","cost":145573,"rating":4.6},
        {"location":"Delhi","guests":115,"venue":"City Banquet","caterer":"Sharma Caterers","decoration":"Luxury","cost":376689,"rating":4.9},
    ]
}


# ---- AI READY DATA ----
past_events = []

for event_type, events in past_events_by_type.items():
    for e in events:
        e["event_type"] = event_type
        past_events.append(e)
