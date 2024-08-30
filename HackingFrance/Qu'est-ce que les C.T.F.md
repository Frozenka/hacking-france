## **Les captures the flag (CTF)**

_Les CTF sont des mises à disposition d’éléments vulnérables tels que des applications, des réseaux, des systèmes d’exploitation et bien d’autres, avec pour objectif de prendre le contrôle maximal de ceux-ci et de récupérer des « flags ». Ces flags sont des preuves que l’on a bien réussi à exploiter les vulnérabilités._

Les CTF sont un excellent moyen de tester et d’améliorer ses compétences. Ils sont souvent plus difficiles que la réalité, car par définition, ceux-ci sont créés de façon vulnérable avec, la plupart du temps, un seul chemin de compromission. Dans la réalité, si vous n’arrivez pas à exploiter une faille lors de votre pentest, il est possible de le faire en passant par une autre voie.

On distingue plusieurs types de CTF :

1. **Les boxs :** Ce sont des représentations de systèmes d’exploitation (Linux, Windows, macOS…) avec des services en exécution comme un serveur web, le partage SMB, etc. La plupart du temps, vous n’avez que l’IP de la machine et vous devez à partir de là trouver le point d’entrée et poursuivre jusqu’à atteindre le plus haut niveau de privilège possible sur cette machine.
    
2. **Les Challenges :** Ils sont plus petits. Par exemple, vous avez un serveur web qui héberge une API ou une application web et vous devez exploiter celle-ci pour obtenir le flag.
    
3. **Les Labs :** Ils sont comme des boxs, mais multiples et intégrés dans un ou plusieurs réseaux. Vous avez en général une IP de réseau et devez trouver le point d’entrée, la bonne machine, etc. Ensuite, vous devez rebondir sur les autres boxs, pivoter sur les différents réseaux, etc., jusqu’à devenir administrateur de domaine et avoir ainsi accès à la totalité des machines.
    

## Les plateformes de CTF

- [**Hackthebox**](https://app.hackthebox.com/) : Une des plateformes les plus connues, avec des boxs, des challenges et des Prolabs. Les boxs récentes sont souvent basées sur les dernières vulnérabilités connues, ce qui en fait un très bon moyen de rester à jour.
    
    [**Tryhackme**](https://tryhackme.com/signup?referrer=63f658bb7ed6fe017647c61d) : L’une des meilleures plateformes pour débuter. Les boxs sont plus faciles que celles de Hackthebox et souvent guidées pas à pas. Vous serez accompagné étape par étape jusqu’à la compromission.
    
    [**Vulnlab**](https://www.vulnlab.com/) : Une plateforme plus réaliste, conçue par XCT, le numéro 1 mondial sur Hackthebox. Le niveau est plus élevé, mais extrêmement enrichissant ! Retrouvez une vidéo de présentation de la plateforme ici : [Vidéo Vulnlab](https://www.youtube.com/watch?v=BIZECU2h-YU).
    
    [**Rootme**](https://www.root-me.org/) : Principalement dédiée aux challenges, c’est l’une des meilleures plateformes de challenges.
    
    [**Tower CTF**](https://tower-ctf.fr/) : Une plateforme développée par un jeune homme talentueux. Très gamifiée, elle permet de réaliser des challenges comme si vous étiez dans un jeu.