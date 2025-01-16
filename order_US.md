# USERSTORY

# place order
En tant que client, je veux pouvoir passer une commande afin de finaliser mon achat et réduire le stock des produits que j'ai ajoutés à mon panier.
Critères d'acceptation :
    Si je passe une commande, le stock des produits est réduit en fonction des quantités commandées
    Un message de confirmation m'indique que la commande a été passée avec succès et le montant total est clairement affiché avec 2 décimales
    Si la commande est passée correctement, les produits sont considérés comme achetés et le stock est mis à jour

# view order
En tant que client, je veux pouvoir consulter le détail de ma commande afin de vérifier les produits et le montant total avant de procéder au paiement.
Critères d'acceptation :
    Si la commande contient des produits, une liste détaillant le nom de chaque produit, sa quantité et le prix total est affichée
    Le montant total de la commande est clairement affiché à la fin de la liste des produits
    Si la commande est vide, un message indiquant qu'aucun produit n'a été commandé est affiché