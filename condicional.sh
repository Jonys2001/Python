#! /bin/bash

read -p "introduce edad " age
echo  "Tu edad es: $age"

: '
si es un IF
    -eq: equals
    -le: lower o equals
    -ge: greather o equals
    -lt: lower than
    -gt: greather than
'

if (($age=22)) || (($age=23))
then 
    echo "tienes 22 o 23  años"
elif [ $age -le 22 ]
    then
        echo "eres menor a 22 años"
else
    echo "no tiene 22 años"
fi




: '

if [ $age -eq 22 ] || [ $age -eq 23 ]
then 
    echo "tienes 22 o 23  años"
elif [ $age -le 22 ]
    then
        echo "eres menor a 22 años"
else
    echo "no tiene 22 años"
fi
'