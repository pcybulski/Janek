#!/bin/bash

if [ -f /dev/shm/minetest ]
 then

echo "\
    1 -> MINETEST \
    2 -> YOUTUBE \
    3 -> HBOGO, BAJKI \
    4 -> MINECRAFT
    "

read choice

else
	echo "Ty mały cwaniaku!!! Przejdz program"
fi


case $choice in

  1)
    /home/jan/minetest.sh
    ;;

  2)
    firefox
    ;;

  3)
    /opt/google/chrome/chrome
    ;;

  4)
    /usr/bin/minecraft-launcher
    ;;


  *)
    echo -n "unknown"
    ;;
esac





