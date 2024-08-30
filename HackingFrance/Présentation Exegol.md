![](https://hacking-france.fr/wp-content/uploads/2024/07/image.png)

Je vais m’efforcer dans ce texte de vous expliquer et de vous démontrer pourquoi, **pour moi**, **Exegol est le meilleur environnement de travail en Pentest** !

Pour commencer, qu’est-ce qu’Exegol ?

---

> Exegol est un environnement de hacking communautaire, puissant et pourtant suffisamment simple pour être utilisé par n’importe qui au quotidien. Exegol est la meilleure solution pour déployer des environnements de hacking puissants de manière sécurisée, facile et professionnelle. Exegol convient aux pentesters, aux joueurs de CTF, aux chasseurs de bogues, aux chercheurs, aux débutants et aux utilisateurs avancés, aux défenseurs, aux utilisateurs élégants de macOS et aux professionnels de Windows en entreprise, ainsi qu’aux utilisateurs puissants de type UNIX.

[**GitHub – ThePorgs/Exegol: Fully featured and community-driven hacking environment**  
_Fully featured and community-driven hacking environment – ThePorgs/Exegol_github.com](https://github.com/ThePorgs/Exegol)

(Retrouvez une présentation d’un de ses créateurs sur ma chaîne ici : [Présentation Exegol Par Shutdown](https://youtu.be/E8TAZ_J_H8s?si=kmOxs9c0Z7DT7fm7) )

### Et concrètement ?

- Il s’agit d’un environnement containériser (via docker ) que nous pouvons lancer (et personnaliser, nous verrons ça plus tard) à la demande pour chaque client, CTF, challenge ou n’importe quoi dont vous auriez besoin d’un environnement ‘propre’.
- Vous aurez directement accès à une gigantesque multitude d’outils pré-installés et pré-configurés (Bloodhound, Burp Suite, Havoc, la suite Impacket et beaucoup d’autres : [lien vers la documentation](https://exegol.readthedocs.io/en/latest/exegol-resources/resources.html)).
- Une multitude de **commandes déjà pré-enregistrées** pour gagner en vitesse, et vous permettra de rapidement utiliser un outil sans forcément devoir reprendre vos notes ou revoir la documentation.
- **Des alias** pour faciliter le lancement de vos outils, et bien sûr le tout directement configuré pour votre environnement.
- Le très gros avantage est que chaque conteneur est **complètement indépendant de votre système** et n’a aucun lien les uns avec les autres. Vous pouvez donc “casser” un conteneur, votre système n’en sera pas impacté. Cela peut aussi être idéal pour tester certains programmes peu sûrs…
- Diverses options incroyablement utiles, comme l’enregistrement du terminal (entrée ET sortie !) horodaté, le **lancement direct de votre VPN** sur le conteneur, un **environnement graphique** accessible par un navigateur (comme une attack box).
- **Des mises à jour** et **améliorations permanentes**, avec une **communauté** bienveillante et réactive !

### – Le cloisonnement

Lors de vos Pentests, **vous devez** (ou devriez) faire en sorte que les données clients recueillies soient complètement en sécurité. Pour cela, la solution la plus courante est de créer un **snapshot de son système** (Kali, par exemple), que vous devez redéployer pour chaque client, et le conserver pendant un certain temps en l’état, et ce, **pour chaque test** !

**Exegol vous permet cela très simplement**, de manière sûre et surtout avec un énorme gain d’espace !

Votre espace restera intact tant que vous ne supprimez pas son conteneur. Vous aurez donc :

- Les programmes utilisés,
- Les versions exactes utilisées le jour et l’heure du test (imaginons un litige avec un client, il vous suffira de rouvrir le conteneur et vous pourrez fournir toutes les informations à votre client),
- L’historique complet,
- Les fichiers récupérés, modifiés, etc.,
- Aucune “pollution” d’un quelconque autre client.

Une fois le délai passé, vous pouvez simplement supprimer le conteneur en quelques secondes. Et vous pouvez en créer autant que vous le souhaitez !

### – Les Outils

Vous aurez une incroyable liste d’**outils pré-installés** (en fonction de la version d’Exegol que vous choisissez). Pourquoi installer Kali avec la totalité de ses outils, alors que vous avez simplement à lancer Exegol et vous aurez ces mêmes outils installés et **prêts à l’emploi** ? La liste des outils ne cesse de s’allonger, elle est **établie par des professionnels** en fonction de leurs besoins quotidiens, il y a donc peu de chances que vous n’ayez pas ce que vous cherchez ! Et si c’était le cas, il vous est quand même possible de l’installer classiquement ! La plupart des outils sont déjà configurés avec des alias, donc pas besoin de taper directement le chemin du script, uniquement son nom.

### Les Options

(Vous trouverez les options [ici](https://exegol.readthedocs.io/en/latest/exegol-wrapper/start.html))

- Vous pouvez lancer directement un VPN dans votre conteneur, sans impacter votre hôte ! simplement avec la commande — vpn=/fichier.ovpn
- Enregistrer la totalité des actions d’entrée et de sortie de votre shell à la seconde près, simplement avec l’option -l
- Il est maintenant aussi possible d’avoir une interface graphique avec Exegol ! Il vous suffit de la définir au lancement du conteneur, ensuite vous accédez directement avec votre GUI depuis un navigateur en vous rendant sur l’adresse IP et le port choisi, et en entrant vos identifiants fournis après l’ouverture de votre conteneur !

### – Personnalisation

Il est possible **très simplement** de lancer un conteneur avec **ses propres options** ! Il vous manque un outil, une source, un alias ou autres ? Vous pouvez simplement gérer cela avec les “**My resources**” : Pour cela, il vous suffit d’éditer les fichiers se trouvant dans : **_~/.exegol/my-resources/_** Vous avez deux dossiers, un pour y déposer vos propres scripts, binaires, etc., et l’autre pour éditer les configurations diverses : _apt, Bloodhound, Firefox, Python3, tmux, vim, zsh…_ Une explication est disponible sur la documentation officielle ici : [lien vers la documentation](https://exegol.readthedocs.io/en/latest/exegol-image/my-resources.html)

---

Pour ma part, j’ai directement créé un dépôt GitHub avec mes propres configurations et modifications de l’environnement, notamment :

- Rajout d’alias
- Rajout d’historique
- Rajout de scripts, binaires, etc.
- Modifications graphiques, j’ai par exemple raccourci le nom du conteneur affiché à l’écran, changé quelques couleurs, etc.
- Modification du fichier tmux

L’avantage de procéder ainsi ? Il me suffit de modifier mon GitHub pour que cela affecte toutes mes futures créations de conteneurs. De cette façon, même si je change d’ordinateur de travail, il me suffit de mettre une seule ligne dans Exegol pour retrouver EXACTEMENT mon flux de travail.

Lien de mon GitHub pour Exegol : [https://github.com/Frozenka/Exegol-Ressources](https://github.com/Frozenka/Exegol-Ressources)

![](https://cdn-images-1.medium.com/max/800/1*81G3XeYD4EAQI7W5K5982A.gif)

GIF de mon flux de travail Exegol

J’espère que cela vous a convaincu ou vous a fait découvrir un magnifique outil, et même si ce n’est pas le cas, je vous invite à le tester par vous-même

### Remerciements :

Pour finir, je tiens à remercier grandement toutes les personnes qui ont participé de près ou de loin à la création et au maintient de cet incroyable outil ! (**Shutdown**, **Dramelac**, **Qu35t** et **bien d’autres…**)

> Exegol, c’est par ici : [https://github.com/ThePorgs/Exegol](https://github.com/ThePorgs/Exegol)

_Et surtout, n’oubliez pas : Exegol4life ._