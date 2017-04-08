#!/bin/bash
sudo apt-get -y install python-pip
sudo pip install termcolor

wget -O ~/vocab-data.json "https://raw.githubusercontent.com/nguyenchien97/learning-vocabulary/master/5000-english-words.json" --no-check-certificate
wget -O ~/vocab.py "https://raw.githubusercontent.com/nguyenchien97/learning-vocabulary/master/vocab.py" --no-check-certificate

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	OSBASHRC=bashrc
elif [[ "$OSTYPE" == "darwin"* ]]; then
	OSBASHRC=bash_profile
fi

if ! grep -Fxq 'python ~/vocab.py' ~/.$OSBASHRC; then
	echo $'python ~/vocab.py' >> ~/.$OSBASHRC
fi

OSBASHRC="zshrc"
if [[ -f ~/.$OSBASHRC ]]; then
	if ! grep -Fxq 'python ~/vocab.py' ~/.$OSBASHRC; then
		echo $'python ~/vocab.py' >> ~/.$OSBASHRC
	fi
fi

