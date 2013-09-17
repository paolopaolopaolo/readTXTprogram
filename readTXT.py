import os, sys, subprocess as sp, re


def linker(pagekey,pn):
	links=re.findall(r"http://[.\w\d\=\?\-\_/\(\)]*",pagekey[pn])
	count=0
	itemkey={}
	print "\nThe following links are on this page!\n"
	print "0...Return To Page\n"
	for item in links:
		count+=1
		itemkey[count]=item
		print str(count)+"..."+str(item)
	
	if len(links)>0:
		openlink=int(raw_input("Open: "))
		try:
			if openlink==0:
				scroller(pagekey,pn)
			else:
				if os.path.exists(r"C:\Program Files\Mozilla Firefox\firefox.exe"):
					sp.call([r"C:\Program Files\Mozilla Firefox\firefox.exe", itemkey[openlink]])
				else:
					print "This program uses Mozilla Firefox. Please make sure you download Firefox.\n"
					print "If you have Firefox and you still receive this message, ensure that the\n"
					print "Program Files are in the following place on your computer:\n"
					print r"C:\Program Files\Mozilla Firefox\firefox.exe"
					scroller(pagekey,pn)
				returntopage=raw_input("Press ENTER to return to page.")
				if returntopage=="":
					scroller(pagekey,pn)
				else:
					linker(pagekey,pn)
		except ValueError:
			print "You've picked a number without a link!\nRETURNING TO PAGE!\n\n\n"
			scroller(pagekey,pn)
		except KeyError:
			print"You've picked a number without a link!\nRETURNING TO PAGE!\n\n\n"
			scroller(pagekey,pn)
	else:
		print "No links found on this page!"
		scroller(pagekey,pn)

def scroller(pagekey,pn):
	scroll=""
	while scroll.upper!="EXIT":
		if pn in pagekey:
			print "\n"
			print pagekey[pn]
			scroll=raw_input("--PAGE:"+str(pn)+"--\n").upper()
			pn+=1
			if scroll.upper()=="GOTO":
				goto(pagekey)
			if scroll.upper()=="BACK":
				pn-=2
				scroller(pagekey,int(pn))
			if scroll.upper()=="LINKS":
				pn-=1
				linker(pagekey,pn)
			if scroll.upper()=="FIND":
				finder(pagekey,pn-1)
			if scroll.upper()=="HELP":
				print"GOTO will bring you to the desired page\n"
				print"HELP will show you this page again\n"
				print"BACK will move you back one page\n"
				print"FIND will help you find pages if you give it a word\n"
				print"LINKS will sniff the page for any links\n"
				print"EXIT will exit the program"
				scroller(pagekey,pn-1)
			if scroll.upper=="EXIT":
				print "GOODBYE!"
				sys.exit(0)
		else:
			print "You've reached the end!"
			startover=raw_input("Start from beginning(Y/N)?")
			if startover.upper()=="Y":
				scroller(pagekey,1)
			elif startover.upper()=="N":
				print "GOODBYE!"
				sys.exit(0)
			else:
				print "Poops!"
				scroller(pagekey,42)


def goto(pagekey):
	try:
		pgnmbr=int(raw_input("What page did you want to skip to?\n"))
		scroller(pagekey,pgnmbr)
	except KeyError:
		print "Try again!(The book probably doesn't have that many pages)\n"
		goto(pagekey)

def finder(pagekey,pn):
	searchterm=raw_input("Search term?\n")
	results=[]
	for key in pagekey:
		match=re.search(searchterm.lower(),pagekey[key].lower())
		if match!=None:
			results.append(key)
	if len(results)<1:
		print "No pages were found with that word!\n"
		scroller(pagekey,pn)
	else:	
		print searchterm.upper() +" was found on the following pages!"
		print results
	
	try:
		goto=int(raw_input("Type in page number to goto page or just press ENTER."))
		scroller(pagekey,goto)
	except (ValueError,KeyError):
		print "Returning to PAGE!"
		scroller(pagekey,pn)

def main():
	#consolidate filenames with spaces in them
	filename=""
	if len(sys.argv)>2:
		addTo=len(sys.argv)
		for i in range(1,addTo):
			filename+=sys.argv[i]+" "
		filename=filename[0:-1]
	else:
		filename=sys.argv[1]

		if os.path.exists(filename):
	#load book into hashfile
			f=open(filename, 'rU')
			viewingwindow=10
			pagekey={0:"Default"}
			pn=1
			while pn>=1 and pagekey[pn-1]!="":
				pagekey[pn]=""
				for i in range(0,viewingwindow):
					pagekey[pn]+=f.readline()
				pn+=1
		else:
			print "Filename not found!"

	#option: start from beginning, or start at page number
		cors=raw_input("Continue from page number(Y/N)?").upper()
		if cors=="Y":
			goto(pagekey)
		elif cors=="N":
			scroller(pagekey,1)
		else:
			print "error!"
			main()

	


if __name__=='__main__':
	main()