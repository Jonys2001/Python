#! /bin/bash

mkdir -p Taller_clase_3/Archivos/Textos_planos
mkdir -p Taller_clase_3/Archivos/Pdf
mkdir -p Taller_clase_3/Mover_imagen_aqui

cd ./Taller_clase_3/Archivos/Textos_planos
touch Texto_plano1.txt
touch Texto_plano2.txt

cd ..
cd ./Pdf
url=http://biblio3.url.edu.gt/Libros/mfis.pdf
curl -o Explicaciones.pdf $url

cd ..
cd ..
url=https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg
curl -o Imagen1.jpg $url

mv Imagen1.jpg ./Mover_imagen_aqui

tree ./ > estructura.txt