#! /bin/bash

mkdir -p ./Tallere_clase_3/Archivos 
mkdir -p ./Tallere_clase_3/Mover_Imagen_aqui

cd ./Taller_clase_3/Archivos
touch texto_plano.txt
echo "Hola Texto Plano" > Texto_plano.txt
cp textp_plano.txt ./Copia_texto_plano.txt

cd..
url=https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg
curl -o Imagen1.jpg $url

mv Imagen1.jpg ./Mover_Imagen_aqui