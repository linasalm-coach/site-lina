#!/usr/bin/env python3
"""Génère index.html à partir des contenus de la plaquette."""
import sys, html
from pathlib import Path

OUT = Path(sys.argv[1])

BILAN_1 = ("1 Bilan Forme (offert)", "30' Entretien + 30' Tests Physiques")
BILAN_PT = ("1 Bilan Forme + 1 PT (offerts)", "30' Entretien + 30' Tests Physiques + 1 séance 60' coaching privé")
REDUC = "<b>Étudiants et -27 ans :</b> une réduction de -5% supplémentaire s’applique à toutes les offres."

# Mettre True pour réafficher les prix sur le site
SHOW_PRICES = False

def prog_cards(items, prices, monthly):
    return [
        dict(title="1 mois", bilan=BILAN_1, items=items, price=prices[0]),
        dict(title="3 mois", stamp="-5%", bilan=BILAN_PT, items=items, price=prices[1], note=f"*Soit env. {monthly[0]}€/mois"),
        dict(title="6 mois", stamp="-10%", bilan=BILAN_PT, items=items, price=prices[2], note=f"*Soit env. {monthly[1]}€/mois"),
    ]

def pt_cards(dur, items, prices):
    return [
        dict(title=f"1 séance PT ({dur})", items=items, price=prices[0]),
        dict(title=f"Carnet de 5 ({dur})", stamp="-5%", items=items, price=prices[1]),
        dict(title=f"Carnet de 10 ({dur})", stamp="-10%", items=items, price=prices[2]),
    ]

SECTIONS = [
    dict(
        id="gymnastique", nav="Gymnastique", big="GYMNASTIQUE",
        collage=["gym-1", "gym-2", "gym-3", "gym-4"], bw=[2],
        photo="gym", photo_alt="Lina aux anneaux",
        intro=["Débloque ta première traction stricte ou renforce ton endurance sur des high skills comme le Bar Muscle Up : peu importe ton niveau, cette programmation est faite pour améliorer tes compétences gymniques en CrossFit.",
               "Cette programmation s’intègre dans une pratique régulière du CrossFit et vient en complément des WOD déjà programmés dans ta box."],
        facts=[("Nombre de séances par semaine", "2 séances - env. 45'-1H max."),
               ("Pré-requis", "Tous niveaux (programmation 100% personnalisée)")],
        cards=prog_cards(["Exercices de renforcement musculaire transférables sur les mouvements en suspension/inversion pour construire une base solide",
                          "Educatifs et Skills pour améliorer ta technique"], [80, 228, 432], [76, 72]),
    ),
    dict(
        id="halterophilie", nav="Haltérophilie", big="HALTÉROPHILIE",
        collage=["halte-1", "halte-2", "halte-3", "halte-4"], bw=[],
        photo="halte", photo_alt="Lina devant une barre d'haltérophilie",
        intro=["Ensemble on va améliorer ta technique et te renforcer pour arriver solide sous tes barres pour exploser tes PR ! (et en flexion complète 😉)",
               "Cette programmation s’intègre dans une pratique régulière dans une box de CrossFit et vient en complément des WOD déjà programmés dans ta box."],
        facts=[("Nombre de séances par semaine", "2 séances - env. 1H"),
               ("Pré-requis", "Tous niveaux (programmation 100% personnalisée)")],
        cards=prog_cards(["1 séance / semaine sur le mouvement de Snatch + Squat",
                          "1 séance / semaine sur le mouvement de Clean&Jerk + Tirage"], [90, 258, 486], [86, 81]),
    ),
    dict(
        id="hybrid", nav="Hybrid", big="HYBRID",
        collage=["hybrid-1", "hybrid-2", "hybrid-3", "hybrid-4"], bw=[0, 2],
        photo="hybrid", photo_alt="Lina en box jump",
        intro=["Tu kiffes woder avec tes copains mais t’es trop frustré.e de ne pas encore avoir les DU ou pouvoir enchainer tes toes to bar ?<br>Ensemble on va identifier tes lacunes pour les travailler spécifiquement et renforcer tes points forts sous fatigue.",
               "Cette programmation s’intègre dans une pratique régulière dans une box de CrossFit et vient en complément des WOD déjà programmés dans ta box."],
        facts=[("Nombre de séances par semaine", "3 séances - env. 1H"),
               ("Pré-requis", "Min. 1 an de CrossFit"),
               ("Les petits +", "Des conseils nutrition, récupération et sommeil pour optimiser tes entraînements et ta progression")],
        cards=prog_cards(["3 séances/s pour améliorer toutes tes qualités physiques : haltéro, gym, metcon"], [120, 342, 648], [114, 108]),
    ),
    dict(
        id="hybrid-plus", nav="Hybrid+", title="Hybrid+",
        photo="hybrid-plus", photo_alt="Compétition de CrossFit, montée à la corde",
        intro=["Si ton objectif est de performer aux Open ou participer à des compétitions de CrossFit, on peut travailler ensemble de manière plus avancée avec une programmation 360° et jouer sur tous les curseurs de ton fitness pour devenir une vraie machine de guerre. 🚀",
               "Une programmation compétition est à destination de profils entraînés : il faut être capable d’encaisser le volume d’entraînement sans se blesser - cette prog. peut s’adapter à des athlètes souhaitant garder quelques WOD programmés dans leur box, si la prog peut être communiquée en amont."],
        facts=[("Nombre de séances par semaine", "5 séances - env. 1H30 - 2H max."),
               ("Pré-requis", "Maîtrise tous les mouvements de CrossFit (hors RMU/HSW) ; athlète Inter/RX+"),
               ("Les petits +", "Des conseils nutrition, récupération et sommeil pour optimiser tes entraînements et ta progression")],
        cards=prog_cards(["5 séances/s pour améliorer toutes tes qualités physiques : haltéro, gym, metcon"], [140, 399, 756], [133, 126]),
    ),
    dict(
        id="personal-training", nav="Personal Training", title_outline="PERSONAL TRAINING", teaser=1,
        photo="personal-training", photo_alt="Lina écrit au tableau de la box",
        intro=["Si tu veux aller plus loin lors de tes entraînements, le personal training (coaching privé) te permettra d’avoir un accompagnement personnalisé et plus avancé soit pour t’aider à débloquer un mouvement soit pour compléter le suivi d’une programmation spécifique avec des corrections immédiates, des éducatifs qu’on travaillera ensemble et un petit coup de motivation pour t’emmener en dehors de ta zone de confort.",
               "Je te propose donc qu’on se retrouve en physique pour une séance de 1H ou 1h30 en fonction des mouvements que tu souhaites travailler. 🏋🏽‍♂️"],
        facts=[],
        tabs=[
            ("1H", pt_cards("1H", ["Séance de 1H coachée en salle",
                                   "Un échauffement spécifique et protocole de mobilité (10-15')",
                                   "Un bloc de travail de force ou technique (20-30')",
                                   "Un bloc de travail cardiovasculaire en circuit training (15')"], [70, 330, 630])),
            ("1H30", pt_cards("1H30", ["Séance de 1H30 coachée en salle",
                                       "Un échauffement spécifique et protocole de mobilité (15')",
                                       "Un bloc de travail technique haltérophilie ou gym (30')",
                                       "Un bloc de travail de force ou renforcement spécifique (30')",
                                       "Un bloc de travail cardiovasculaire en circuit training (15')"], [90, 425, 810])),
        ],
    ),
    dict(
        id="remise-en-forme", nav="Remise en forme", big="Remise en forme/<br>Perte et prise de poids", big_mixed=True,
        collage=["forme-1", "forme-2", "forme-3", "forme-4"], bw=[0, 2],
        photo="forme", photo_alt="Écran d'un SkiErg",
        title="Remise en forme<br>Perte et prise de poids",
        intro=["Tu souhaites te remettre en forme, perdre du gras ou prendre de la masse de façon durable et efficace.",
               "Je te propose un accompagnement à distance, 100 % adapté à ton niveau et à ton rythme. Les séances sont simples, progressives et pensées pour t’aider à retrouver un corps plus fort, plus tonique et que tu sois plus en forme dans ta vie de tous les jours !"],
        facts=[("Nombre de séances/semaine", "4 séances – env. 1h"),
               ("Pré-requis", "Aucun – adapté aux débutants comme aux niveaux intermédiaires"),
               ("Les petits +", "Conseils nutrition &amp; récupération ; Suivi régulier &amp; ajustements hebdomadaires")],
        suivi=True,
    ),
]

def e(s):  # texte déjà rédigé à la main, on laisse passer <br> et entités
    return s

def card_html(c, best=False):
    stamp = f'<span class="stamp">{c["stamp"]}</span>' if c.get("stamp") else ""
    flag = '<p class="flag">Meilleur prix</p>' if best and SHOW_PRICES else ""
    bilan = ""
    if c.get("bilan"):
        bilan = f'<p class="gift"><b>{c["bilan"][0]}</b><small>{c["bilan"][1]}</small></p>'
    lis = "".join(f"<li>{i}</li>" for i in c["items"])
    note = f'<p class="note">{c["note"]}</p>' if c.get("note") and SHOW_PRICES else ""
    price = f'<p class="price">{c["price"]}<span>€</span></p>' if SHOW_PRICES else ""
    cta = "Réserver sur Instagram" if SHOW_PRICES else "Demander le tarif"
    return f'''<div class="card-wrap{" best" if best else ""}">{stamp}<article class="card">
        {flag}<h4>{c["title"]}</h4>
        {price}{note}
        {bilan}<ul>{lis}</ul>
        <a class="card-cta" href="https://www.instagram.com/toomanyburpees/" target="_blank" rel="noopener">{cta}</a>
      </article></div>'''

def cards_html(cards):
    return '<p class="swipe">Glisse pour voir les autres formules →</p><div class="cards">' + "".join(card_html(c, k == len(cards) - 1) for k, c in enumerate(cards)) + '</div>'

def collage_html(s):
    imgs = ""
    for k, name in enumerate(s["collage"]):
        cls = f"c{k+1}" + (" bw" if k in s["bw"] else "")
        imgs += f'<img class="{cls}" src="img/{name}.jpg" alt="" loading="lazy">'
    return f'''<div class="collage" aria-hidden="true">{imgs}
      <p class="collage-title">{s["big"]}</p></div>'''

SUIVI = '''<div class="suivi">
  <h3 class="anton">un suivi personnalisé</h3>
  <div class="suivi-grid">
    <div><svg viewBox="0 0 48 48" aria-hidden="true"><g fill="#fff" stroke="#1d1d1b" stroke-width="1.4"><path d="M10 9l20-3 5 31-20 3z"/><path d="M13 7h20v32H13z"/><path d="M16 5h20v32H16z"/></g><g stroke="#9aa8bf" stroke-width="1"><path d="M19 11h14M19 14h14M19 17h14M19 20h14M19 23h14M19 26h10M19 29h12"/></g></svg>
      <h4 class="anton">bilan forme &amp; tests</h4><hr>
      <p>Le bilan forme est <b>offert</b> pour toute souscription à une programmation.</p>
      <p>Il comporte 30' d’entretien (objectifs, lifestyle, antécédents) et 30' de tests (mobilité, proprioception, endurance...)</p></div>
    <div><svg viewBox="0 0 48 48" aria-hidden="true"><rect x="8" y="30" width="7" height="12" fill="#e6dccf"/><rect x="17" y="24" width="7" height="18" fill="#cbb5a0"/><rect x="26" y="16" width="7" height="26" fill="#8e735b"/><rect x="35" y="8" width="7" height="34" fill="#4a3d32"/></svg>
      <h4 class="anton">suivi hebdomadaire</h4><hr>
      <p>J’ai un regard sur tous les retours effectués sur les séances programmées pour ajuster et optimiser de semaines en semaines</p>
      <p>La programmation n’est pas gravée dans le marbre et évoluera en même temps que toi.</p></div>
    <div><svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="20" fill="#cbb5a0"/><path d="M17 14c-2 1-3 3-2 6 2 6 7 11 13 13 3 1 5 0 6-2l-4-4-3 2c-3-1-6-4-7-7l2-3z" fill="#fff"/><path d="M27 15a7 7 0 0 1 6 6M27 11a11 11 0 0 1 10 10" stroke="#fff" stroke-width="1.6" fill="none"/></svg>
      <h4 class="anton">disponibilité</h4><hr>
      <p>Je suis joignable pour répondre à tes questions (jours ouvrés) via Whatsapp, mail ou téléphone.</p></div>
  </div>
</div>'''

def section_html(n, s):
    out = f'<section class="presta" id="{s["id"]}" data-num="{n}">'
    if s.get("title_outline"):
        h = f'<h2 class="outline">{s["title_outline"]}</h2>'
    else:
        h = f'<h2>{s.get("title", s["nav"])}</h2>'
    facts = "".join(f"<li><b>{k} :</b> {v}</li>" for k, v in s["facts"])
    facts = f'<ul class="facts">{facts}</ul>' if facts else ""
    t = s.get("teaser", 0)
    teaser = f'<p>{s["intro"][t]}</p>'
    rest = "".join(f"<p>{p}</p>" for k, p in enumerate(s["intro"]) if k != t)
    more = f'<details class="more"><summary>En savoir plus</summary><div class="lead">{rest}</div>{facts}</details>'
    out += f'''<div class="presta-head">
      <div class="presta-text">{h}<div class="lead">{teaser}</div>{more}</div>
      <figure class="presta-photo"><img src="img/{s["photo"]}.jpg" alt="{s["photo_alt"]}" loading="lazy"></figure>
    </div>'''
    if s.get("cards"):
        out += cards_html(s["cards"]) + f'<p class="reduc">{REDUC}</p>'
    if s.get("tabs"):
        btns = "".join(f'<button role="tab" aria-selected="{"true" if i == 0 else "false"}" data-tab="{s["id"]}-{t}">Séance de {t}</button>' for i, (t, _) in enumerate(s["tabs"]))
        panels = "".join(f'<div class="tabpanel" id="{s["id"]}-{t}" {"" if i == 0 else "hidden"}>{cards_html(c)}</div>' for i, (t, c) in enumerate(s["tabs"]))
        out += f'<div class="tabs" role="tablist">{btns}</div>{panels}<p class="reduc">{REDUC}</p>'
    if s.get("suivi"):
        out += SUIVI
        out += '<div class="devis"><p class="devis-t anton">Tarif sur devis</p><p>Chaque accompagnement est construit selon ton objectif : écris-moi pour en parler.</p><a class="btn" href="https://www.instagram.com/toomanyburpees/" target="_blank" rel="noopener">Demander un devis sur Instagram</a></div>'
    out += "</section>"
    return out

NAV = [("qui-suis-je", "Qui suis-je ?")] + [(s["id"], s["nav"]) for s in SECTIONS]

navlinks = "".join(f'<a href="#{i}">{label}</a>' for i, label in NAV) + '<a class="cta" href="#contact">Contact</a>'
sections = "".join(section_html(k + 2, s) for k, s in enumerate(SECTIONS))

PAGE = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coaching Lina Salmi El Idrissi · Prestations &amp; tarifs</title>
<meta name="description" content="Programmations CrossFit (gymnastique, haltérophilie, hybrid, compétition), personal training et remise en forme. Tarifs 2026-27.">
<meta property="og:title" content="Coaching Lina Salmi El Idrissi">
<meta property="og:description" content="Prestations &amp; tarifs 2026-27">
<meta property="og:image" content="img/couverture.jpg">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23cbb5a0'/%3E%3Ctext x='16' y='24' font-family='Impact,sans-serif' font-size='22' text-anchor='middle' fill='%23111'%3EL%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:ital,wght@0,400;0,600;0,700;1,400;1,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="bar">
  <a class="logo" href="#top">coaching<small>Lina Salmi El Idrissi</small></a>
  <nav class="navlinks" aria-label="Sections">{navlinks}</nav>
</header>


<main id="top">
<section class="cover">
  <div class="cover-text">
    <h1>coaching<span>LINA SALMI EL IDRISSI</span></h1>
    <hr>
    <p>Tarifs &amp; Prestations 2026 - 27</p>
  </div>
  <figure class="cover-photo"><img src="img/couverture.jpg" alt="Lina Salmi El Idrissi assise au sol de la box, en train d'écrire une programmation" fetchpriority="high"></figure>
</section>



<section class="presta" id="qui-suis-je" data-num="1">
  <div class="presta-head">
    <div class="presta-text">
      <h2>Qui suis-je ?</h2>
      <blockquote class="lead">
        <p>“Je n’ai jamais vraiment été sportive. J’ai découvert le CrossFit à 25 ans et ça a radicalement changé ma vie.<br>J’ai commencé les compétitions très tôt, notamment en équipe et j’ai décidé de me spécialiser pendant une pleine saison en haltérophilie.</p>
      </blockquote>
      <details class="more"><summary>Lire la suite</summary><blockquote class="lead">
        <p>De là, j’ai acquis énormément de connaissances dans la discipline, ce qui me permet de suivre spécifiquement des athlètes qui souhaiteraient peaufiner leur technique et exploiter leur plein potentiel en CrossFit.</p>
        <p>Quand je coache, mon seul but, c’est d’égayer la journée des gens et leur prouver qu’ils sont capables d’accomplir de grandes choses. Mon accompagnement va au delà d’une simple séance pour se défouler : <b>mon objectif c’est que vous soyez fiers de vous.</b> ❤️ ”</p>
      </blockquote></details>
      <ul class="facts plain">
        <li><b>Diplôme :</b> BPJEPS AF Mention Haltérophilie &amp; Musculation</li>
        <li><b>Pratique Sportive :</b> CrossFit (+20 compétitions) ;<br>Haltérophilie (Niveau IRG -69) - Streetlifting (débutante)</li>
      </ul>
    </div>
    <figure class="presta-photo"><img src="img/qui-suis-je.jpg" alt="Lina aux anneaux" loading="lazy"></figure>
  </div>
</section>



{sections}

<section class="contact" id="contact">
  <div class="contact-inner">
    <h2>LET’S DO THIS TOGETHER ! 🚀</h2>
    <p class="who">LINA SALMI EL IDRISSI</p>
    <ul class="contact-links">
      <li><a href="https://www.instagram.com/toomanyburpees/" target="_blank" rel="noopener">Écris-moi sur Instagram</a></li>
      <li><a href="https://www.instagram.com/toomanyburpees/" target="_blank" rel="noopener">@toomanyburpees</a></li>
      <li><a href="mailto:linasalmi.coach@gmail.com">linasalmi.coach@gmail.com</a></li>
      <li><a href="tel:+33608117307">+33 6 08 11 73 07</a></li>
    </ul>
  </div>
</section>
</main>

<footer class="foot">
  <p>© Lina Salmi El Idrissi · Coaching · Tarifs 2026-27 · <a href="#mentions" onclick="document.getElementById('mentions').open=true">Mentions légales</a></p>
  <details id="mentions">
    <summary>Mentions légales</summary>
    <p><b>Éditrice du site :</b> Lina Salmi El Idrissi, entrepreneur individuel, coach sportive diplômée (BPJEPS AF Mention Haltérophilie &amp; Musculation).<br>
    SIREN : 852 914 167<br>
    Contact : <a href="mailto:linasalmi.coach@gmail.com">linasalmi.coach@gmail.com</a> · +33 6 08 11 73 07</p>
    <p><b>Hébergement :</b> GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
    <p><b>Photos et textes :</b> © Lina Salmi El Idrissi. Toute reproduction est interdite sans autorisation.</p>
    <p><b>Données personnelles :</b> ce site ne dépose aucun cookie et ne collecte aucune donnée. Les échanges ont lieu par Instagram, mail ou téléphone.</p>
  </details>
</footer>

<a class="fab" href="https://www.instagram.com/toomanyburpees/" target="_blank" rel="noopener" aria-label="Écrire à Lina sur Instagram">Instagram</a>

<script>
// onglets Personal Training
document.querySelectorAll('.tabs').forEach(function (list) {{
  list.addEventListener('click', function (ev) {{
    var b = ev.target.closest('button'); if (!b) return;
    list.querySelectorAll('button').forEach(function (x) {{
      var on = x === b; x.setAttribute('aria-selected', on);
      document.getElementById(x.dataset.tab).hidden = !on;
    }});
  }});
}});
// section active dans la barre
var links = {{}};
document.querySelectorAll('.navlinks a').forEach(function (a) {{ links[a.getAttribute('href').slice(1)] = a; }});
var io = new IntersectionObserver(function (entries) {{
  entries.forEach(function (en) {{
    if (!en.isIntersecting) return;
    Object.values(links).forEach(function (a) {{ a.classList.remove('on'); }});
    var a = links[en.target.id]; if (!a) return;
    a.classList.add('on');
    var nav = a.parentNode;
    nav.scrollTo({{left: a.offsetLeft - nav.clientWidth / 2 + a.offsetWidth / 2, behavior: 'smooth'}});
  }});
}}, {{rootMargin: '-45% 0px -50% 0px'}});
document.querySelectorAll('main section[id]').forEach(function (s) {{ io.observe(s); }});
</script>
</body>
</html>
'''

OUT.joinpath("index.html").write_text(PAGE, encoding="utf-8")
print("ok")
