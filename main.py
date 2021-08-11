import sys



def banner():
	"""
	this function should print the banner
	"""
	pass
	

		
	print("██╗░░░░░██╗███████╗░█████╗░██████╗░██████╗░██╗░██████╗  ░██╗░░░░░░░██╗██╗░░░░░███╗░░░███╗")
	print("██║░░░░░██║╚════██║██╔══██╗██╔══██╗██╔══██╗╚█║██╔════╝  ░██║░░██╗░░██║██║░░░░░████╗░████║")
	print("██║░░░░░██║░░███╔═╝███████║██████╔╝██║░░██║░╚╝╚█████╗░  ░╚██╗████╗██╔╝██║░░░░░██╔████╔██║")
	print("██║░░░░░██║██╔══╝░░██╔══██║██╔══██╗██║░░██║░░░░╚═══██╗  ░░████╔═████║░██║░░░░░██║╚██╔╝██║")
	print("███████╗██║███████╗██║░░██║██║░░██║██████╔╝░░░██████╔╝  ░░╚██╔╝░╚██╔╝░███████╗██║░╚═╝░██║")
	print("╚══════╝╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░░░░╚═╝")
	print("email: 0liver.7he.1izard@gmail.com\ngithub: https://github.com/the-liz4rd")



def usage():
	"""
	this function should print the usage of the tool and the default
	"""
	print("""
		Default: --small-needed --number-needed --capital --length-at-least 0 --length-at-most 100 -o wordlist_output.txt
		
		--wpa				-w	Password list for WPA and WPA2 wifis, most have both capital and small letters

		--capital			-c	Might include capital letters
		--no-capital			Without any capital letters
		--need-capital          Must include capital letters
		--small				-s  Might include small letters
		--no-small              Without any small letters
		--need-small            Must include small letters
		--number			-n  Might include numbers
		--no-number             Without any numbers
		--need-number           Must include numbers

		--input				-i  Path to a File including raw words
		--output			-o  Path to the output file

		--length-at-least       Least allowed length for the passwords
		--length-at-most        Most allowed length for the passwords

		--best-performance	-b	best performance mode provides less words but with less probability of a successful attack
		--most-probale		-m	most probable mode provides more words than best performance but with more probability of a successful attack
		""")






def write_output (file_name, final_wordlist):
    with open(file_name, 'w') as f:
        for sth in final_wordlist:
            f.write(sth + "\n")


def main():
	arg_list = sys.argv
	arg_list.remove(sys.argv[0])

	n=0
	raw_words = []

	# --------------------------------------------------------------------------------
	# --no-small:    there should not be any small letters       =>  small_status=0
	# --small:       there might be some small letters           =>  small_status=1
	# --need-small:  there have to be at least one small letter  =>  small_status=2

	# same thing is true for "number" and "capital" 
	# --------------------------------------------------------------------------------

	# defaults:
	small_status = 2
	capital_status = 1
	number_status = 2

	banner()

	least_len = ""
	most_len = ""
	output_file = ""
	input_file = ""


	if len(arg_list) == 0:
		usage()
		exit()

	best_performance = False
	most_probable = False

	for arg in arg_list:
		n=n+1
		if arg.startswith("-"):
			if arg == "-o" or arg == "--output" :
				output_file = arg_list[n]
			elif arg == output_file:
				pass
			elif arg == "--length-at-least":
				try:
					least_len = int(arg_list[n])
				except :
					print("[-] ERROR: length-at-least most be a number")
					usage()
					exit()
			elif arg == "--length-at-most":
				try:
					most_len = int(arg_list[n])
				except:
					print("[-] ERROR: length-at-most most be a number")
					usage()
					exit()
			elif arg == "-w" or arg == "--wpa":
				capital_status = 2
				number_status = 2
				small_status = 2
				most_len = 16
				least_len = 8
			elif arg == "-c" or arg == "--capital":
				capital_status = 1
			elif arg == "-s" or arg == "--small":
				small_status = 1
			elif arg == "-n" or arg == "--number":
				number_status = 1
			elif arg == "--no-number":
				number_status = 0
			elif arg == "--no-small":
				small_status = 0
			elif arg == "--no-capital":
				capital_status = 0
			elif arg == "--need-number":
				number_status = 2
			elif arg == "--need-small":
				small_status = 2
			elif arg == "--need-capital":
				capital_status = 2
			elif arg == "-i" or arg == "--input":
				input_file = arg_list[n]
			elif arg == "-h" or arg == "--help":
				usage()
				exit()
			elif arg == "-b" or arg == "--best-performance":
				best_performance = True
			elif arg == "-m" or arg == "--most-probable":
				most_probable = True
			else :
				print("[!] no such argument")
				banner()
				exit()
		elif arg == output_file:
			pass
		elif arg == most_len:
			pass
		elif arg == least_len:
			pass
		elif arg == input_file:
			pass
		else:
			raw_words.append(arg)



	if len(raw_words) == 0:
		print("[-] ERROR: No input word was found")
		usage()
		exit()


	if input_file:
		print(f"[*] Trying to read input words from the given file name: {input_file}")
		try:
			nothin = open(input_file, "r").read().split("\n")
			print("[+] Done.")
			raw_words = nothin
		except:
			print("[-] ERROR: an error occured while reading the file")
			exit()


	if not output_file:
		print("[-] No Given name for output file")
		print("[+] Using default name(wordlist_output.txt")
		output_file = "wordlist_output.txt"

	if not least_len:
		print("[-] No Given number for least possible length")
		least_len = 0

	if not most_len:
		print("[-] No Given number for most possible length")
		most_len = 100



	numbers = [] # only numbers
	lowers = [] # words with only small letters
	uppers = [] # words with only capital letters
	capitals = [] # words with both capital and small letters



	print("[*] Preparing raw words")


	for sth in raw_words:
		try:
			sth2 = int(sth)
			numbers.append(sth)
			if len(sth) >= 5 : numbers.append(sth[:-4])
			if len(sth) >= 9 : numbers.append(sth[:-8])
			if len(sth) >= 5 : numbers.append(sth[:4])
		except:
			if sth != "":
				sth2 = sth
				uppers.append(sth.upper())
				lowers.append(sth.lower())
				capitals.append(sth.capitalize())
			if len(sth) >= 3 :
				sth2 = sth[:2]
				uppers.append(sth2.upper())
				lowers.append(sth2.lower())
				capitals.append(sth2.capitalize())
			if len(sth) >= 2 :
				sth2 = sth[0]
				uppers.append(sth2.upper())
				lowers.append(sth2.lower())



	print("[+] Done.")
	print("[*] Generating the word list")

	wordlist = []


	all_words = uppers + lowers + capitals + numbers

	all_words.append("")
	if most_probable:
		for word1 in all_words:
			for word2 in all_words:
				for word3 in all_words:
					wordlist.append(word1+word2+word3)
	elif best_performance:
		for word1 in all_words:
			for word2 in all_words:
				wordlist.append(word1+word2)
	else:
		for word1 in all_words:
			for word2 in all_words:
				for word3 in all_words:
					wordlist.append(word1+word2+word3)




	print("[+] Done.")
	print("[*] Removing the useless words")





	final_wordlist = []

	if number_status == 0:
		if small_status == 0:
			if capital_status == 0:
				print("[!] ERROR: No word can be generated with these arguments!!")
				usage()
				exit()
			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
		elif small_status == 1:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.islower():
							if word.isalpha():
								final_wordlist.append(word)
			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # Sh1234
			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # Sh1234

		elif small_status == 2:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # Sh1234

			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								final_wordlist.append(word)
							else:
								pass # Sh1234




	elif number_status == 1:
		if small_status == 0:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

		elif small_status == 1:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)

			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)

		elif small_status == 2:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
							if word.isupper():
								if word.isalpha():
									pass # SH
								else:
									pass # SH1234
							elif word.islower():
								if word.isalpha():
									final_wordlist.append(word)
								else:
									final_wordlist.append(word)
							elif word.isnumeric():
								pass # 1234
							else:
								if word.isalpha():
									final_wordlist.append(word)
								else:
									final_wordlist.append(word)
	#-------------------------------------------------------------------------
			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								final_wordlist.append(word)
							else:
								final_wordlist.append(word)



	elif number_status == 2:
		if small_status == 0:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

		elif small_status == 1:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								final_wordlist.append(word)
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								final_wordlist.append(word)
						elif word.isnumeric():
							final_wordlist.append(word)
						else:
							if word.isalpha():
								pass # Sh
							else:
								final_wordlist.append(word)

			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								final_wordlist.append(word)
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								final_wordlist.append(word)

		elif small_status == 2:
			if capital_status == 0:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								final_wordlist.append(word)
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								pass # Sh1234

			elif capital_status == 1:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								final_wordlist.append(word)
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								final_wordlist.append(word)

			elif capital_status == 2:
				for word in wordlist:
					if len(word) <= most_len and len(word) >= least_len:
						if word.isupper():
							if word.isalpha():
								pass # SH
							else:
								pass # SH1234
						elif word.islower():
							if word.isalpha():
								pass # sh
							else:
								pass # sh1234
						elif word.isnumeric():
							pass # 1234
						else:
							if word.isalpha():
								pass # Sh
							else:
								final_wordlist.append(word)


	print("[+] Done.")

	print("[*] Creating the file and Writing words to the output file...")
	write_output(file_name=output_file, final_wordlist=final_wordlist)
	print("[+][+] Done")

if __name__ == '__main__':
    main()