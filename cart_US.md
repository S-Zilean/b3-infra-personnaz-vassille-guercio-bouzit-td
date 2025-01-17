# USERSTORY

# add product
En tant qu'utilisateur, je veux pouvoir ajouter des produits à mon panier, à condition que la quantité demandée soit disponible en stock, afin de pouvoir les acheter
Critères d'acceptation :
    Si la quantité demandée dépasse le stock disponible, un message d'erreur est retourné
    Si la quantité demandée est inférieure ou égale au stock disponible, le produit est ajouté au panier avec la quantité spécifiée

# remove product
En tant qu'utilisateur, je veux pouvoir supprimer des produits de mon panier, afin de pouvoir ajuster mes choix avant de finaliser ma commande.
Critères d'acceptation :
    Si le produit est présent dans le panier, il est supprimé
    Si le produit n'est pas présent dans le panier, un message d'erreur est retourné

# calculate total
En tant qu'utilisateur, je veux connaître le total de ma commande en calculant la somme des prix des produits dans mon panier, afin de savoir combien je dois payer.
Critères d'acceptation :
    Le total est calculé en fonction de la quantité de chaque produit et de son prix unitaire
    Le total est renvoyé sous forme numérique
    
# display cart
En tant qu'utilisateur, je veux pouvoir voir le contenu de mon panier sous forme d'une liste avec le nom du produit, la quantité et le prix total par produit, afin de vérifier ce que j'ai ajouté avant de passer à la commande.
Critères d'acceptation :
    Si le panier est vide, un message indiquant "Votre panier est vide." est affiché
    Si le panier contient des produits, une liste détaillant chaque produit avec sa quantité et son prix total est affichée