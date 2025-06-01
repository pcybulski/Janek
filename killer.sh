#!/usr/bin/bash

### Script checking if program for learning reading/typing/math was executed if not then it will kill the bowser or games

if [ ! -f /dev/shm/minetest ]

then
	ps aux | egrep "mari0|chrome|firefox|mintest|minetest|pingus|minecraft" | egrep -v "grep|Pulpit|kitty|python|tmux|sleep" | awk '{print $2}' | xargs -i kill -9  {}


fi

