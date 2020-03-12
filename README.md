# Projet_TDD

## Objectifs

créer une API permettant d'accéder aux données d'une base en lecture et écriture.

Cette base contiendrait des données d'équipements avion comme des systèmes (appelés LRU), des sous systèmes (appelés SRU) et les avions ou les lignes de produit auxuquels ils correspondent.

L'API sera utilisée par la suite pour créer une application de gestion d'équipements (stock, doc de maintenance/réparations, prix etc) gérés par Thales au sein de l'équipe ILS. Elle sera également mise à disposition pour l'entreprise au cas où d'autres équipes auraient besoin de l'utiliser pour d'autres besoins.

## Routes :

`/home` : page d'accueil de l'API

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

`/addProductLine` : send a request to add a product line in the database

`/addSystemName` : send a request to add a system name in the database

`/addAirframer` : send a request to add a airframer in the database

`/addAircraft` : send a request to add a aircraft in the database

`/addLruDenom` : send a request to add a lru denomination in the database

`/addSruDdenom` : send a request to add a sru denomination in the database

`/addLRU` : send a request to add a LRU in the database

`/addLRU` : send a request to add a SRU in the database

`/editProductLine` : send a request to edit an existing product line

`/editSystemName` : send a request to edit an existing system name

`/editAirframer` : send a request to edit an existing airframer

`/editAircraft` : send a request to edit an existing aircraft

`/editLruDenom` : send a request to edit an existing lru denomination

`/editSruDenom` : send a request to edit an existing sru denomination

`/editLRU` : send a request to edit an existing LRU

`/editSRU` : send a request to edit an existing SRU

`/removeProductLine` : send a request to remove a product line

`/removeSystemName` : send a request to remove a system name

`/removeAirframer` : send a request to remove an airframer

`/removeAircraft` : send a request to remove an aircraft

`/removeLruDenom` : send a request to remove a lru denomination

`/removeSruDenom` : send a request to remove a sru denomination

`/editLRU` : send a request to remove a LRU

`/editSRU` : send a request to remove a SRU

