@echo off
SET URI=

echo Importando productos...
mongoimport --uri %URI% --collection productos --type csv --headerline --file ./data/productos.csv

echo Importando combos...
mongoimport --uri %URI% --collection combos --type csv --headerline --file ./data/combos.csv

echo Importando restaurantes...
mongoimport --uri %URI% --collection restaurantes --type csv --headerline --file ./data/restaurantes.csv

echo Importando usuarios...
mongoimport --uri %URI% --collection usuarios --type csv --headerline --file ./data/usuarios.csv

echo Importando ordenes...
mongoimport --uri %URI% --collection ordenes --type csv --headerline --file ./data/ordenes.csv

echo Importando resenias...
mongoimport --uri %URI% --collection resenias --type csv --headerline --file ./data/resenias.csv

echo Importacion completa
pause
