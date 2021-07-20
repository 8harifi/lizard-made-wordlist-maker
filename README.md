# lizard-made-wordlist-maker
this tool doesn't require any installation.
just download using 'git clone https://ginhub.com/the-lizard-py/lizard-made-wordlist-maker' and run the main.py file like this 'python3 main.py'
		
usage:

		--wpa              -w   Password list for WPA and WPA2 wifis, most have both capital and small letters

		--capital          -c   Might include capital letters
		--no-capital            Without any capital letters
		--need-capital          Must include capital letters
		--small            -s   Might include small letters
		--no-small              Without any small letters
		--need-small            Must include small letters
		--number           -n   Might include numbers
		--no-number             Without any numbers
		--need-number           Must include numbers
		--input            -i   Path to a File including raw words
		--output           -o   Path to the output file
		--length-at-least       Least allowed length for the passwords
		--length-at-most        Most allowed length for the passwords
    
    
    Default: --small-needed --number-needed --capital --length-at-least 0 --length-at-most 100 -o wordlist_output.txt

installation:

    git clone https://github.com/the-liz4rd/lizard-made-wordlist-maker.git    
    cd lizard-made-wordlist-maker/
    python3 setup.py install
    wordlist_maker --help # to make sure that the module is installed

this tool is very fast and also very easy to use
and it will also remove any useless word that you don't need, for instance if you need passowrds for a dictionary attack on a wifi hanshake, you won't get very short or very long passwords, or any password only including numbers or small letters will be removed :) you're welcome
