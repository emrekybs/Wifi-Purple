read -p $' AP name (max=16): ' AP_name

read -p $' Dictionary name: ' dictionary_name

printf " Number of APs: 100\n"

printf " Dictionary created successfully >\e[1;32m $(pwd)/$dictionary_name\e[0m\n"

for i in {1..100};
do 
    echo "$AP_name-$i"; 
done > $dictionary_name
