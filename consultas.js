//-------------
// Comandos para importar datos a MongoDB desde archivos CSV
//Importando productos...
mongoimport --uri %URI% --collection productos --type csv --headerline --file ./data/productos.csv

//Importando combos...
mongoimport --uri %URI% --collection combos --type csv --headerline --file ./data/combos.csv

//Importando restaurantes...
mongoimport --uri %URI% --collection restaurantes --type csv --headerline --file ./data/restaurantes.csv
//Importando usuarios...
mongoimport --uri %URI% --collection usuarios --type csv --headerline --file ./data/usuarios.csv

//Importando ordenes...
mongoimport --uri %URI% --collection ordenes --type csv --headerline --file ./data/ordenes.csv

//Importando resenias...
mongoimport --uri %URI% --collection resenias --type csv --headerline --file ./data/resenias.csv
