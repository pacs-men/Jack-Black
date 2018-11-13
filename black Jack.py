"""
$$$$$$$\  $$\                     $$\                $$$$$\                     $$\       
$$  __$$\ $$ |                    $$ |               \__$$ |                    $$ |      
$$ |  $$ |$$ | $$$$$$\   $$$$$$$\ $$ |  $$\             $$ | $$$$$$\   $$$$$$$\ $$ |  $$\ 
$$$$$$$\ |$$ | \____$$\ $$  _____|$$ | $$  |            $$ | \____$$\ $$  _____|$$ | $$  |
$$  __$$\ $$ | $$$$$$$ |$$ /      $$$$$$  /       $$\   $$ | $$$$$$$ |$$ /      $$$$$$  / 
$$ |  $$ |$$ |$$  __$$ |$$ |      $$  _$$<        $$ |  $$ |$$  __$$ |$$ |      $$  _$$<  
$$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\       \$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
\_______/ \__| \_______| \_______|\__|  \__|       \______/  \_______| \_______|\__|  \__|

"""

"""
"""
Règles utilisées:

Joueurs: Nombre n de jours contre le croupier
Début:
Tous les joueurs sauf le croupier misent une somme d'argent x
tous les joueur en incluant le croupier recoivent 2 cartes face découvertes
venant du meme packet composé d'un nombre c de packet de 52 cartes

Tour:
-Tous les joueur on un choix soit de piocher une nouvelle carte soit de s'arreter
(le joueur s'arrete automatiquement si son score est sup ou egaul a 21)
-Si le score du croupier est inférieur a 17 il pioche un carte sinon il s'arette
- et le tour recommence avec les joueur qui ne ce sont pas arrété
comptage du score:
le comptage du score est fait automatiquement si le joueur a des as
le score le plus avantageux pour lui est calculé
Fin:
une foit que tous les joueurs et le croupier ont finit de joueur:
pour chaque joueur:
-si son score est égual a 21 le joueur gagne 2x sa mise
-si son score est supérieur a celui du croupier et inférieur à 21
 il gagne 2x sa mise
-si son score est egual a celui du croupier il reprend sa mise
-si son score est inferieur a celui du croupier ou supérieur a 21 il
 perd sa mise

 
"""
"""

#colors = ["♣", "♦", "♥", "♠"]

print("♣")
