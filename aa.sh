#!/bin/bash

FONTCFG=~/.config/fontconfig/
mm_kb=https://github.com/naingyeminn/mm-kb/archive/master.zip
wget -N $mm_kb 2> /dev/null || curl -OL $mm_kb
unzip -o master.zip
cd mm-kb-master
sudo apt install make ibus-table -y
sudo make install
ibus-daemon -rdx
im-config -n ibus
mkdir -p $FONTCFG
cp /usr/share/mmfs/fonts.conf $FONTCFG

#!/bin/bash