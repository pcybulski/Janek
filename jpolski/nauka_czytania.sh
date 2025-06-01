#! /bin/bash

#gnome-terminal -- bash -c "python3.8 ./nauka_czytania.py; exec bash"

directory=`/home/jan/minetest`
echo $directory
gnome-terminal -- bash -c "cd $directory && python3.8 /home/jan/minetest/nauka_czytania.py; exec bash"

