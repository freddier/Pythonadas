# -*- coding: utf-8 -*-
import imaplib, re

# you want to connect to a server; specify which server
server= imaplib.IMAP4_SSL('imap.googlemail.com')
# after connecting, tell the server who you are
server.login('email@dominio.com', 'password')
# this will show you a list of available folders
# possibly your Inbox is called INBOX, but check the list of mailboxes
code, mailboxen= server.list()
# print mailboxen
# if it's called INBOX, then…
server.select("Rebotes")
r, data = server.search(None, "ALL")
lista = ""
mails=0
for num in data[0].split():
    mails += 1
    try:
        rs, mensaje = server.fetch(num, "(RFC822)")
    except:
        print "fuck... " + str(num)
        continue
    email =  mensaje[0][1]
    match = re.search("Failed-Recipients: .*?\r", email, re.MULTILINE|re.DOTALL)

    #Si hay match, es decir, si hay failed recipients
    if(match is not None):
        match = match.group(0).replace("Failed-Recipients: ", "").strip()
        #print match

        #Si no es un mail repetido, lo agregamos. 
        if(lista.find(match) == -1):
            lista += match + "\n"
        # Cada 50 mails, escribimos en el archivo y seguimos tranquilitos
        if(mails % 50 == 0):
            f = open("errores.txt", "w")
            f.write(lista)
            f.close()
            print str(mails) + " procesados [" + str(num) + "]"


