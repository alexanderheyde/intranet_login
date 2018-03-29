import mechanize
import urllib2

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

def form_finder():
	url = raw_input('Welche URL moechten Sie untersuchen? ') 	//to find the login form
	br.open(url)
	for form in br.forms():
		print 'Formular Name:', form.name
		print form

def login():
	print 'Intranet Login'
	user = raw_input('Benutzername eingeben: ')
	passw = raw_input('Passwort eingeben: ')
	br.open('url')	 				 //enter intranet URL
 	br.select_form(nr=2)				 //enter form number
	br.form['user'] = user
	br.form['pass'] = passw
	br.submit()
	for link in br.links():
		if link.text == 'ONLINE Stundenplan':
			return link.url
			break
#       example = open('/home/pi/example.txt') 		//to show a sample source
#       for text in example:
#               print text

def read_timetable():
	url = login()
	response = urllib2.urlopen(url)
	page = response.read()
	print page

def menu():
	print '1. Formular finden'
	print '2. Stundenplan anzeigen'
	auswahl = input('Zahl eingeben: ')
	if auswahl == 1:
		form_finder()
	elif auswahl == 2:
		read_timetable()
	else:
		print 'Eingabe fehlgeschlagen. '
		menu()

menu()
