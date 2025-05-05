@echo off
SET URI=mongodb+srv://angel:angel123@cluster0.krfnzqa.mongodb.net/restaurante

echo Importando productos...
mongoimport --uri %URI% --collection productos --type json  --file ./data/productos.json --jsonArray

echo Importando combos...
mongoimport --uri %URI% --collection combos --type json --file ./data/combos.json --jsonArray

echo Importando restaurantes...
mongoimport --uri %URI% --collection restaurantes --type json --file ./data/restaurantes.json --jsonArray

echo Importando usuarios...
mongoimport --uri %URI% --collection usuarios --type json  --file ./data/usuarios.json --jsonArray

echo Importando ordenes...
mongoimport --uri %URI% --collection ordenes --type json  --file ./data/ordenes.json --jsonArray

echo Importando resenias...
mongoimport --uri %URI% --collection resenias --type json  --file ./data/resenias.json --jsonArray

echo Importacion completa
pause
