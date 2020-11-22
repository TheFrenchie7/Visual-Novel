# Déclarez les personnages utilisés dans le jeu.
define k = Character('Kazuki', color="#0000CC")
define s = Character('Sawano', color="#c8ffc8")
define m = Character('Masuyama')
define sa = Character ('Saeki', color="#33CC00")
define n = Character ('Nagase', color="#CC6666")

# Le jeu commence ici
label start:

    scene black

    "ATTENTION ! Tout les choix que vous allez faire impactera l'histoire. À vous d'en assumer les conséquences."

    hide black

    show bedroom2
    with dissolve

    "07/09/2020 - 6h45"

    "*Biiiip biiip biiip biiip !*"

    k "Hmmm..."

    "6h45... C'est trop tôt."

    "Je suis arrivé tard hier soir dans ce dortoir."

    k "Aujourd'hui c'est la première fois que je vais dans ce lycée."

    "C'est bientôt les vacances d'été mais pourtant j'ai été transferé dans se lycée."

    "Parce que soi-disant je causais trop de problème à mon ancienne école."

    k "Bon, je n'ai pas le choix. Allons-y"

    hide bedroom2

    show entrance
    with dissolve

    "07/09/2020 - 7h45"

    "Fille 1" "Ah, j'espère que je trouverai bientôt le prince charmant."

    "Fille 2" "Hihi ! Tu es trop tête en l'air pour ça."

    k "Pffff..."

    "Fille 1" "Hiiiiiii ! *chuchote* C'est qui lui ?"

    k "*regarde* Tch..."

    "Fille 2" "*peur* *chuchote* Je sais pas, baisse la tête et le regarde pas, restons pas la."

    "Et voilà ça commence déjà, premier jour, première fois que je viens, on me juge déjà."

    "Juste parce que j'ai la même expression que lui... Je ne l'est jamais connu, pourtant je n'ai eu que des problèmes à cause de lui."

    "Même si..."

    k "*soupir* Ah ! Je ne comprends pas pourquoi les gens sont si intéresser par l'amour..."

    m "Hé ! Kazami !"

    k "Ah !"

    "Lui s'est Yuji Masuyama, c'est la seul personne que je connais dans cette école, on s'est déjà croisé deux trois fois dans le train."

    "Quand je lui est annoncé que j'allais être transferé ici, il était très surpris, mais il était content aussi va savoir pourquoi."

    m "Bonjour ! Alors encore tout seul ?"

    k "Hmmm..."

    show sprite1 at right
    with dissolve

    "Je remarque qu'une fille nous observait du coin de l'oeil mais je n'y prêta pas attention."

    m "Allez viens faudrait pas qu'on soit en retard. Puis avec un nouveau départ comme ça tu pourra te faire plein d'amis."

    k "Mouais. J'en doute."

    hide sprite1
    with dissolve

    hide entrance

    show classroom
    with dissolve

    "07/09/2020 - 8h30"

    "Sensei" "Bonjour tout le monde, je vous présente Kazami Kazuki."

    "Sensei" "C'est le nouvelle étudiant qui nous rejoins à partir d'aujourd'hui."

    "Sensei" "J'espère que vous serai sympa avec lui, va t'assoir Kazami."

    "Hmmm... première rangée, dernière place à côté de la fenêtre."

    "Sensei" "Bien commençons"

    hide classroom

    scene black
    with dissolve

    hide black

    show classroom
    with dissolve

    "07/09/2020 - 12h30"

    m "Hé ! Kazami, tu viens on va manger"

    "Garçon 1" "T'es sur Yuji ?"

    k "Non c'est bon je vais aller sur le toit, et puis je fais peur à t'es amis... Tch, on se voit plus tard."

    m "D'accord à plus tard !"

    hide classroom

    show roof
    with dissolve

    k "Il n'y a personne parfait."

    "Je m'installa dans un coin et commença à fermer les yeux."

    scene black

    "C'est ma façon à moi de me déconnecter de ce monde qui me rejette et de me sentir mieux"

    "J'entendis la porte du toit s'ouvrir..."

    s "Hmmm... On m'a dit qu'il était la."

    "Je n'y prêta pas attention, mais j'entendis des bruits de pas se rapprocher jusqu'à moi."

    k "Qu'est-ce tu veux ?"

    hide black

    show roof

    show sprite2
    with dissolve

    s "Hum... Je cherche un certain Kazami et on m'a dit qu'il était ici. Tu sais pas où je pourrais le trouver ?"

    k "Et tu lui veux quoi ?"

    s "Euh s'est un truc par rapport à Yuji-kun..."

    k "Pfff..."


    menu choix:

        "L'aider":
            jump aide

        "Ne pas l'aider":
            jump confirmation


label confirmation:
    "Tu es sûr ?"

    hide sprite2

    show sprite16

    menu:
        "Oui":
            jump bad1

        "Non":
            jump choix

label aide:

    k "Bon... c'est moi Kazami. C'est quoi le problème avec Yuji ?"

    hide sprite2

    hide sprite16

    show sprite4

    s "Eh bien... C'est pas un problème... Mais comme on dirait que tu es proche de lui, tu pourrai peut-être m'aider ?"

    k "Ce n'est pas comme si j'étais son meilleur ami, mais je peux lui en toucher deux mots si tu veux."

    hide sprite4

    show sprite5

    s "Merci beaucoup !"

    k "Tu t'appelle comment au faite ?"

    hide sprite5

    show sprite1

    s "Yumi Sawano !"

    k "Bien je t'arrangerai quelque chose, tu peux partir maintenant."

    hide sprite1

    show sprite6

    s "Bien sûr, y a pas de soucis. Merci encore !"

    hide sprite6

    k "*soupir*"

    hide roof

    jump continu


label bad1:

    k "Non je sais pas où il est."

    s "Oh... D'accord"

    hide sprite16
    with dissolve

    "Tu n'entendis plus jamais parler d'elle."

    hide roof

    scene black
    with dissolve

    "FIN"

    return

label continu:
    show classroom_afternoon
    with dissolve

    "07/09/2020 - 16h30"

    "Les autres étudiants n'ont pas arrêter de me jeter des regards. J'ai peut-être l'habitude mais c'est perturbant à chaque fois."

    k "Yuji ! On rentre ensemble se soir ? J'ai besoin de te parler."

    m "Mais y a pas de soucis, pour une fois que tu le demande je peux pas refuser."

    k "Ouais..."

    hide classroom_afternoon

    show train
    with dissolve

    show sprite44 at right
    with dissolve

    k "Y a quelqu'un qui nous regarde depuis tout à l'heure."

    m "Ah oui ! Elle s'est Ai-chan, s'est la capitaine de l'équipe de Volley-ball."

    k "Mais tu connais tout le monde toi."

    m "Ahah ! n'exagère pas voyons."

    hide sprite44
    with dissolve

    hide train

    show street_afternoon
    with dissolve

    m "Alors tu voulais parler de quoi ?"

    k "Hum... Tu vois qui sais Yumi-chan ?"

    m "Ah oui bien sûr, qu'est-ce qu'elle a ? Attends ne me dis pas que..."

    k "Hein ?"

    m "Me dis pas que t'es amoureux d'elle ?"

    k "Quoi mais pas du tout, c'est plutôt le contraire..."

    m "Donc s'est elle qui t'aime !"

    k "Mais laisse moi finir ! Pfff donc je disais, elle à l'air d'avoir un penchant pour toi, même si je ne comprends pas pourquoi"

    m "Dis pas de bétises Kazami voyons."

    k "Je suis sérieux."

    m "Je ne parle pas de ça, je parle de ce que tu as dit après."

    m "Pourquoi dis tu que ça sert à rien ?"

    k "Parce que l'amour n'est rien d'autre que la pour faire du mal."

    m "Tu es trop coincé Kazuki. Bien j'irai lui parler demain."

    k "Bon bah je te laisse alors à demain."

    m "D'accord à demain."

    hide street_afternoon

    show classroom
    with dissolve

    "08/09/2020 - 8h00"

    "Une journée qui ressemble comme les autres."

    show sprite44
    with dissolve

    sa "Salut ! Je me présente, je m'appelle Ai Saeki, ravi de te rencontrer !"

    "C'est la fille du train, qu'est-ce qu'elle veut."

    k "Hum... Ouais salut moi s'est..."

    hide sprite44

    show sprite40

    sa "Kazami Kazuki, je sais déjà qui tu es ahah."

    k "Ah... Euh d'accord, et qu'est-ce qui t'amène ?"

    hide sprite40

    show sprite39

    sa "Hum... Je peux m'installer à côté de toi aujourd'hui ? Enfin je t'y oblige pas hein si ça te dérange dis le moi."

    "C'est vrai que la place à côté de moi est vide."

    menu:

        "Accepter":
            jump accepter

        "Refuser":
            jump refuser

label accepter:

    k "Oui tu peux t'assoir la, y a pas de soucis."

    hide sprite39

    show sprite44

    sa "Merci beaucoup !"

    "Elle posa son sac et s'installa."

    k "Mais t'es sûr que ça va pas déranger Sensei si tu change de place comme ça, sans demander ?"

    sa "Ne t'inquiète pas pour ça, si ça se trouve il le remarquera même pas."

    k "Hum..."

    hide sprite40

    show sprite36

    k "Je peux te poser une question ?"

    hide sprite36

    show sprite44

    sa "Oui bien sûr !"

    k "Comment ça se fait que tu me connais déjà ?"

    hide sprite44

    show sprite37

    sa "Ah... C'est que... Euh..."

    hide sprite37

    show sprite40

    sa "Oui ! Voilà ! S'est parce que il y a tellement de rumeurs qui circule sur toi que... Euh... Qui ne connaît pas Kazami-kun ahah."

    sa "*chuchotement* et ce n'est bien sûr pas parce que je t'observe depuis que t'es arrivé."

    k "Tu as dis quelque chose ?"

    sa "Non du tout ahah, tu dois sûrement te tromper."

    "La suite de la discussion se passa plutôt bien. Jusqu'à ce que le cours commence."



    jump continu1


label refuser:

    hide sprite39

    show sprite37

    sa "Ah..."

    hide sprite37

    show sprite40

    sa "Ce n'est pas grave ahah, est-ce que je peux te proposer au moins si tu veux venir manger avec moi ce midi ?"

    menu choix1:
        "Accepter":
            jump repas_Ai

        "Refuser":
            jump warning

label warning:
    "Vous êtes sûr ?"

    menu:

        "Oui":
            jump refus

        "Non":
            jump choix1

label repas_Ai:

    k "Bon d'accord."

    sa "Oui merci !"

    sa "On se voit après le cours."

    k "Oui bien sûr."

    hide sprite40

    "Le cours se passa bien mais je senti que le regard d'Ai-chan était constament poser sur moi durant le cours."

    show sprite44

    sa "On y va ?"

    k "Ouais allons-y"

    jump continu2

label refus:

    k "Non désoler."

    hide sprite40

    show sprite37

    sa "Il a refusé..."

    k "Ai...Chan ?"

    hide sprite37

    show sprite54

    sa "Je ne le laisserai pas seul..."

    "Elle me pris le bras et me tiras à travers le couloir."

    k "Ai ! Lâche moi !"

    jump continu3

label continu1:

    hide sprite40

    show sprite44

    sa "On mange ensemble ? Koyamasu-kun ?"

    k "Euh..."

    hide sprite44

    show sprite40

    sa "Allez viens tu n'a pas le choix de toute façon !"

    k "*soupir* Bien d'accord."

    hide sprite40

    hide classroom

    show corridor
    with dissolve

    show sprite54

    sa "On va aller sur le toit, on sera que tout les deux comme ça."

    jump rencontre

label continu2:

    hide classroom

    show corridor
    with dissolve


    hide sprite44

    show sprite44
    with dissolve

    sa "T'a une idée de où on pourrait aller ?"

    k "On peut aller sur le toit ? Y a personne à chaque fois."

    hide sprite44

    show sprite54

    sa "Oh ! j'ai compris tu veux qu'on soit que tout les deux, tout seul, petit coquin."

    k "Pas du tout, je ne pensais pas à ça, s'est juste que c'est un endroit calme et tranquille."

    sa "Hmmm bien sûr."

    jump rencontre

label continu3:

    hide classroom

    show corridor
    with dissolve

    hide sprite54

    show sprite54
    with dissolve

    sa "On va aller sur le toit, tu verras se sera super, on sera que tout les deux."

    jump rencontre

label rencontre:

    "Au détour de la cage d'escalier pour aller sur le toit, une fille apparut dans le coin."

    hide sprite54
    with dissolve

    show sprite19 at left
    with dissolve

    k "Attention !"

    hide sprite19

    show sprite20
    with dissolve

    n "AAAAAAH !"

    "Avant d'avoir pu l'éviter, nous nous rentrons dedans et toutes les feuilles qu'elle avait avec elle tombit par terre."

    n "Aïe..."

    k "Aïe... Oh désolé excuse moi. Ai-chan tu peux aller devant je te rejoins juste après."

    show sprite55 at right
    with dissolve

    sa "Je veux pas !"

    k "Pardon...?"

    hide sprite55

    show sprite40
    with dissolve

    sa "Ah... Non rien, d'accord mais drague pas trop hein ahah."

    k "Ouais... C'est ça"

    hide sprite40
    with dissolve

    "Elle parta mais je senti encore ça présence qui nous épier du regard."

    k "Je suis désolé, ça va ?"

    "Je lui tendis la main pour la relever."

    show sprite23
    with dissolve

    n "Oh non ne t'excuse pas, s'est moi qui ne regardait pas où j'allais."

    "Elle me pris la main, je sentis qu'elle était timide, mais ça peau était douce."

    show sprite55 at left
    with dissolve

    sa "*chuchote* Elle lui à pris la main."

    hide sprite55
    with dissolve

    k "Non vraiment je m'excuse, j'aurais du m'arrêter plus tôt. Je vais t'aider avec t'es feuilles pour me rattraper."

    hide sprite23

    show sprite35

    n "Oh non ne t'embête pas"

    "Elle se baissa en même temps que moi et nos mains se toucha une nouvelle fois."

    hide sprite35

    show sprite20

    n "Ah ! Excuse moi !"

    k "Hum... T'inquiète pas."

    "Je récupéra les feuilles et les lui donna."

    hide sprite20

    show sprite35

    n "Qui est-tu au faite ?"

    show sprite55 at left
    with dissolve

    sa "*chuchote* Elle lui parle en plus."

    hide sprite55
    with dissolve

    k "Kazami Kazuki, Je suis en 1-C et toi ?"

    n "Je suis Echiko Nagase. C'est moi qui m'occupe du conseil des élèves."

    k "Oh d'accord, si ça te dérange pas je vais y aller mon amie doit certainement m'attendre."

    hide sprite35

    show sprite19

    n "Ah oui ! Bien sûr, y a pas de soucis on se verra tout l'heure comme on n'est dans la même classe."

    k "Oh... D'accord, bon bah à plus tard."

    hide sprite19
    with dissolve

    jump lunch

label lunch:

    hide corridor

    show roof
    with dissolve

    "Je rejoignis Ai-chan sur le toit, puis on se trouva une place et commença à manger."

    "La conversation était tout à fait normal, sauf que à un moment."

    show sprite44
    with dissolve

    sa "Dit Koyamasu-kun, je peux te poser une question un peu personnel ?"

    k "Hum ?"

    sa "Est-ce que t'a une petite amie ?"

    k "Quoi ? Pourquoi tu veux savoir ça ?"

    hide sprite44

    show sprite40

    sa "Oh pour rien, pour rien... Je suis juste curieuse."

    k "Non je n'en n'ai pas."

    hide sprite40

    show sprite39

    sa "Vraiment ?"

    k "Oui vraiment."

    hide sprite39

    show sprite54

    sa "C'est parfait... *chuchote* Il sera qu'a moi."

    "Je la regarda suspicieusement après se qu'elle à dit. Elle remarqua mon regard."

    hide sprite54

    show sprite37

    sa "Ah... Euh..."

    hide sprite37

    show sprite40

    sa "Non non, il n'y a rien, c'est juste je voulais dire, je ne te crois pas."

    k "Et pourtant c'est la vérité."

    hide sprite40

    show sprite36

    sa "Mais je trouve que tu es tellement gentil, beau. Tout le monde voudrait être avec toi."

    "Ça dernière phrase me fit rire."

    k "Alors tu ne connais pas beaucoup de choses sur moi."

    sa "Hein ?"

    k "Tout le monde s'arrête qu'a la première impression me concernant, juste car j'ai la même expression facial que lui..."

    k "Je fais peur à tout le monde à cause de ça s'est pour ça que je suis souvent seul."

    sa "Mais se n'est pas possible, tu ne peux pas dire ça..."

    "Je l'interrompis avec un signe de la main."

    k "N'essaye pas, ça ne sert à rien, je te remercie de m'aider quand même."

    hide sprite31

    show sprite37

    k "Mais ça à toujours été le même schéma, toujours tout seul partout où que j'aille."

    k "Le seul qui a toujours été à mes côtés et qui m'a accepté comme je suis est Yuji-kun."

    k "Je n'ai jamais eu d'autre personnes que lui."

    "Après que j'aille dis ça, un silence embarrassant s'installa entre nous."

    "Après un long moment..."

    hide sprite37

    show sprite36

    sa "Bon je vais te laisser, j'ai quelque chose à faire. On se voit à la fin des cours ?"

    k "Ouais pourquoi pas."

    sa "Super, à tout à l'heure."

    hide sprite36
    with dissolve

    "Après qu'elle sois partie, je ferma les yeux, et me plongea dans mon monde, le seul qui m'accepte."

    hide roof

    show corridor_afternoon
    with dissolve

    "08/09/2020 - 15h30"

    "Je suis resté tellement longtemps sur le toit, les yeux fermés, que je n'ai pas vu le temps passer."

    "Avant même que je m'en rends compte, s'était déjà la fin de la journée."

    "Je retourna à la salle de classe pour récupérer mon sac et partir."

    show sprite20
    with dissolve

    n "Ah ! Kazami t'es la."

    "Echiko-chan apparue dans le couloir et courut jusqu'a moi."

    hide sprite20

    show sprite19

    n "Enfin je t'es trouvé. J'ai t'es chercher partout."

    k "Ah bon ? Pourquoi ?"

    hide sprite19

    show sprite35

    n "Eh bien, en tant que présidente du conseil des élèves et qu'on n'est dans la même classe et bien je me demandais où tu était passé."

    "Elle s'inquièter pour moi hein, après tout elle fait son boulot de présidente."

    k "Ouais excuse-moi, je me suis juste assoupi un moment sur le toit et quand je me suis réveiller s'était déjà la fin de la journée."

    "Elle me donna une petite tape dans l'épaule"

    n "Pfff, qu'est-ce que tu peut-être idiot Koyamasu-kun."

    "On se mit tout les deux à rire, comme si on n'était des amis de longue date."

    "Elle est si gentille avec moi."

    n "Bon eh bien puisque tu es la, ça te dirais de venir m'aider ? J'ai juste 2 petits trucs à régler pour le conseil."

    menu:
        "Aider":
            jump conseil

        "Ne pas aider":
            jump refus1


label conseil:

    k "Ouais, tant que je suis la ça serait sympa de passer du temps avec toi."

    hide sprite35

    show sprite23

    n "Super ! Tu verras c'est vraiment trois fois rien."

    "Elle commença à avancer dans le couloir et se dirigea vers une salle de classe. Je fis de même."

    hide sprite23

    hide corridor_afternoon

    show classroom_afternoon
    with dissolve

    "Deux cartons se trouvait à l'intérieur."

    show sprite19
    with dissolve

    n "Est-ce que tu peux les apporter pour moi dans la salle du conseil s'il te plaît."

    k "Y a pas de soucis."

    "Je pris les deux cartons avec moi, puis on se dirigea vers la salle du conseil."

    hide sprite19
    with dissolve

    hide classroom_afternoon

    show corridor_afternoon
    with dissolve

    show sprite35
    with dissolve

    n "Alors, Kazami-kun comment ce passe t'es premier jours dans cette école ?"

    k "Eh bien, ça ne change pas de mon ancienne école..."

    n "Comment ça ?"

    k "Disons que les gens sont toujours autant effrayer par moi."

    n "Ah bon ? je trouve que tu fais pas si peur que ça moi."

    "Inconsciement je posa ma main sur sa tête et commença à frotter ça tête."

    k "T'es bien gentille présidente, la majorité des personnes détourne le regard quand je les croises."

    "Et tu ferai la même chose si tu connaissait mon secret"

    n "Ah... Euh Kazami-kun"

    hide sprite35

    show sprite22

    n "C'est pas que ça me dérange... Mais euh pourrait-tu enlever t'a main s'il te plaît ?"

    k "Ah désoler j'ai pas fais attention."

    "C'est peut-être parce que elle est petite que j'ai fais ça."

    hide sprite22

    show sprite23

    n "Y a pas de soucis c'est juste que ça ma surpris c'est tout."

    hide sprite23

    show sprite19

    n "On y est pose les la je m'occupe du reste, merci pour tout encore, à demain."

    k "D'accord à demain."

    hide sprite 19

    jump sawaclass

label refus1:

    k "Euh... Ne le prends pas mal, mais j'avais prévu d'aller voir quelqu'un après avoir récupérer mon sac."

    hide sprite35

    show sprite19

    n "Oh je vois, eh bien ce n'est pas grave."

    "Elle à l'air déçu..."

    k "Mais je serai ravi de t'aider une prochaine fois bien sûr."

    n "Ahah oui ! Bon eh bien je ne te retiens pas plus longtemps."

    "Elle se dirigea vers une salle de classe et rentra dedans."

    k "Bon il faut que j'aille récupéré mon sac."

    jump sawaclass

label sawaclass:

    hide sprite19

    hide corridor_afternoon

    show classroom_afternoon
    with dissolve

    "J'entra dans la classe et me dirigea vers mon bureau pour récupérer mon sac."

    show sprite3 at left
    with dissolve

    s "Ah Kazami-kun, t'es enfin là !"

    k "Tu m'attendais ?"

    "Elle m'attendait mais pourquoi ?"

    hide sprite3

    show sprite1

    s "Bah oui tu veux que se soit qui d'autre ?"

    k "Je sais pas, Masuyama peut-être ?"

    hide sprite1

    show sprite6

    s "Ah non non, ce qui est important pour l'instant c'est toi, pas lui."

    "Pourquoi elle réagis comme ça ? Il s'est passer quelque chose de mal ?"

    menu:
        "Demander":
            jump tears
        "Ne pas demander":
            jump ignore

label tears:

    k "Excuse-moi mais pourquoi dis-tu ça ?"

    s "Rien... Rien du tout."

    "Je la regarda avec un air suspicieux."

    k "Vraiment ?"

    hide sprite6

    show sprite15

    s "Oui vraiment."

    "Des larmes commença à couler sur ses joues."

    k "Hé ! Pleure pas. Qu'est-ce qui y a ? Tu peux tout me dire tu sais."

    "Je la pris dans mes bras et elle posa ça tête contre mon torse."

    hide sprite15

    show sprite16

    s "Il est venu me voir hier à la fin des cours. J'étais tellement contente mais..."

    "Elle ravala un sanglot et enfouie encore plus ça tête 'dans mon torse'. "

    s "Avant même que je puisse dire quoi que ce soit..."

    s "Il m'a dit qu'il avait aucun sentiment pour moi et qu'il en avait pour une autre fille."

    s "Puis il est parti comme ça."

    "Je leva les yeux en l'air pour exprimer ma désaprobation face à tout ça."

    "Je passa ma main dans ses cheveux et les lui caressa."

    k "La. Tout va bien ce passer, ce n'est pas grave t'inquiète pas."

    "Ses larmes commencèrent à ce calmer et je regarda dehors."

    k "Il commence à ce faire tard, je vais t'accompagner à la station d'accord ?"

    "Elle secoua ça tête et on sorti de l'école pour se diriger vers la station."

    jump railnight


label ignore:

    "Vaut mieux pas demander."

    k "Hmm... Je vois."

    s "On peut rentré ensemble s'il te plaît ? ça m'aidera à me sentir mieux."

    k "Y a pas de soucis."

    "J'attrapa mes affaires et ont sorti de l'école."

    jump railnight

label railnight:

    hide classroom_afternoon

    hide sprite16

    hide sprite6

    show railn
    with dissolve

    show sprite18
    with dissolve

    k "Tu vas mieux ?"

    s "Oui ! Grâce à toi !"

    k "Y a pas de soucis."

    s "Dis tu fais quelque chose ce week-end ?"

    k "...Je sais pas encore si j'ai quelque chose de prévu."

    s "Eh bien tu m'envoie un message hein."

    k "Ouais."

    s "Merci encore de m'avoir raccompagné jusqu'ici, à plus tard."

    k "Bye."

    hide sprite18
    with dissolve

    hide railn

    show bedroom2
    with dissolve

    k "Aaaah..."

    show pistolet1

    "..."

    hide pistolet1

    show rifle1

    k "Je vais devoir y aller..."

    "Voici mon boulot."

    "À suivre..."

    jump chap2

label chap2:

    "Voici ma vie"

    return
