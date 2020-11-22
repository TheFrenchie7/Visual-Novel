init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

init:
     $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

# Déclarez les personnages utilisés dans le jeu.
define o = Character('Ôgami', color="#000000")
define e = Character('Eiko', color="#a40691")
define t = Character('Tessa', color="#4bb60a")
define a = Character('Alicia', color="#e80c0c")


# Le jeu commence ici
label start:

    "Chapitre 1: Un nouveau mystérieux."

    show entrance
    with dissolve

    "Je m'appelle Ôgami Rei à compter d'aujourd'hui je suis un étudiant japonais dans cet école."

    show sprite001
    with dissolve

    "C'est une école pour les gens qui posséde des pouvoirs. On les appels des 'Espers'."

    "Je suis ici car il paraîtrait que j'ai un pouvoir."

    "Mais je suis ressorti de l'exam d'entré avec le rang F."

    "Ce qui veut dire que je n'ai aucun pouvoir."

    "Mais mon année ici n'allait pas être de tout repos."

    hide sprite001
    with dissolve

    # musique d'ambiance

    show alicia_normal
    with dissolve

    a "Hé toi ! Attends moi !"

    o "..."

    a "Oh ! C'est à toi que je parle."

    o "Qu'est-ce qu'il y a vice-présidente ?"

    a "Ne crois pas que je vais te laisser tranquille comme ça."

    o "*soupir* vous avez vu comme moi , je suis ressorti avec le rang F, ce qui veut dire que je posséde pas de pouvoir."

    a "Je suis sûr que t'en as un."

    a "Je me suis pas trompé, je sais ce que j'ai vu."

    "Cette personne ici présente qui est entrain de m'acculer s'est Alicia Redd."

    "Elle posséde le rang S qui est le plus haut rang qu'on peut atteindre de façon normal."

    "Elle est non seulement la vice-présidente du conseil des élèves mais aussi la personne qui aurait vu que j'ai fais usage d'un pouvoir."

    "Par conséquent c'est elle qui ma ramener ici."

    a "De toute façon je vais pouvoir te surveiller partout où tu sera, car j'ai fait en sorte de placer dans ma classe."

    o "..."

    a "Je t'ai à l'oeil, fais gaffe à ce que tu fais."

    hide alicia_normal
    with dissolve

    show tessa_normal at right
    with dissolve

    t "Alors ce serait lui l'étudiant que nous à ramener Alicia-chan intéressant."

    hide tessa_normal
    with dissolve

    show saegusa_normal at left
    with dissolve

    e "Hmmm..."

    hide saegusa_normal
    with dissolve

    hide entrance

    show classroom
    with dissolve

    "Sensei" "Alors tout le monde, nous avons un nouveau étudiant transférer aujourd'hui."

    "Sensei" "Vas-y présente toi."

    o "Ôgami Rei."

    "Sensei" "Ahahah d'accord... bien t'a place est à côté de Redd-chan. Si il a des questions tu l'aideras."

    "Sensei" "Alors pour aujourd'hui..."

    show alicia_normal at left
    with dissolve

    a "T'aurais pu faire un effort sur t'a présentation."

    o "..."

    a "Tu te retrouve à côté de moi, comme ça c'est plus facile pour te surveiller."

    o "..."

    a "T'es pas très bavard dis-moi."

    o "Arrête de me parler c'est tout."

    a "Ok ok j'ai compris, mais à la pause déjeuner on fera le tour du lycée d'accord ?"

    o "..."

    hide alicia_normal
    with dissolve

    "*ding ding* *ding ding*" # song de cloche

    show alicia_normal
    with dissolve

    a "Bon aller Ôgami on n'y..."

    hide alicia_normal

    show alicia_anger

    a "Il a trouvé le moyen de me filer entre les doigts, j'y crois pas."

    hide alicia_anger
    with dissolve

    hide classroom

    show corridor
    with dissolve

    o "(Enfin j'ai réussi à me retrouver tout seul.)"

    "Délinquant 1" "Comment ça le nerd t'as pas ce que je t'ai demandé."

    "Nerd" "Euh..."

    "Délinquant 1" "Réponds-moi."

    "*paf*" with Shake((0, 0, 0, 0), 0.5, dist=30) # tremblement de caméra

    "Nerd" "AÏE !!"

    o "Toi, tu fais quoi ?"

    "Délinquant 1" "Hein ?"

    o "Je t'es poser une question."

    "Délinquant 1" "Qu'est ce que tu me veux toi ?"

    o "..."

    "Délinquant 1" "Tu n'est qu'un rang F, tu n'as aucun droit de me donner des ordres."

    "Délinquant 1" "Tu vas voir ! ...Hein il est passer où ?"

    "*paf*"  with Shake((0, 0, 0, 0), 0.5, dist=50) # tremblement de caméra

    "Délinquant 1" "Aaargh."

    o "Ne le frappe plus jamais et si jamais tu dit à quelqu'un se qui vient de se passer, je te finis."

    "Délinquant 1" "OUUII !! *cours*" # bruit de course

    show tessa_surprise
    with dissolve

    t "Whoa... Il s'est passer quoi à l'instant là."

    t "Y avait quelque chose de bizarre avec lui à l'instant, mais je ne saurais dire quoi."

    t "Il faut que je rapporte ça à la reine."

    hide tessa_surprise
    with dissolve

    return
