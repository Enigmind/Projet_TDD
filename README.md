# Projet_TDD

## Objectifs

créer une API permettant d'accéder aux données d'une base en lecture et écriture.

Cette base contiendrait des données d'équipements avion comme des systèmes (appelés LRU), des sous systèmes (appelés SRU) et les avions ou les lignes de produit auxuquels ils correspondent.

L'API sera utilisée par la suite pour créer une application de gestion d'équipements (stock, doc de maintenance/réparations, prix etc) gérés par Thales au sein de l'équipe ILS. Elle sera également mise à disposition pour l'entreprise au cas où d'autres équipes auraient besoin de l'utiliser pour d'autres besoins.

## Routes :

`/` : page d'accueil de l'API

`/getProductLine` : get a specific Product Line

`/getSystemName` : get a specific System name

`/getAirframer` : get a specific Airframer

`/getAircraft` : get a specific Aircraft

`/getLruDenom` : get a specific LRU Denomination

`/getSruDenom` : get a specific SRU denomination

`/getLRU` : get a specific LRU

`/getSRU` : get a specific SRU

`/getAllProductLines` : get a list of all the existing product lines

`/getAllSystemNames` : get a list of all the existing system names

`/getAllAirframers` : get a list of all the existing airframers

`/getAllAircrafts` : get a list of all the existingaircrafts

`/getAllLRUsDenoms` : get a list of all the existingLRU denominations

`/getAllSRUsDenoms` : get a list of all the existing SRU denominations

`/getAllLRUs` : get a list of all the existing LRUs

`/getAllSRUs` : get a list of all the existing SRUs

`/addElement` : send a request to add a specified element in the database

`/editElement` : send a request to edit an specified element

`/removeElement` : send a request to remove a specified element

D'autres routes seront créées ultérieurement afin d'accéder à des données servant à générer des statistiques. Des regroupements de données par exemple.