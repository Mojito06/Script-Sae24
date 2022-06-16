
#import des modules
import mysql.connector as mariadb
import sys
import os




################################################################################################# FONCTIONS ##################################################################################################

def identif(prenom, nom):
	prenom = prenom[0]
	if len(nom) > 7:
		nom = nom[0]+nom[1]+nom[2]+nom[3]+nom[4]+nom[5]+nom[6]
	ident = prenom+nom
	return ident





###### Photo #######

def photo(test, user, the_cursor):

    )



def suppPhoto(tab,the_cursor):
	if tab[0] != 'Null':
		delete_request = "DELETE FROM Photo WHERE ID = "+tab[0]+""
		select_request = "SELECT ID FROM Photo WHERE test = '"+tab[0]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"
	elif tab[1] != 'Null' and tab[2] == 'Null' and tab[3] == 'Null':
		delete_request = "DELETE FROM Photo WHERE test = '"+tab[1]+"'"
		select_request = "SELECT ID FROM Photo WHERE test = '"+tab[1]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"

	elif tab[1] != 'Null' and tab[2] != 'Null' and tab[3] == 'Null':
		delete_request = "DELETE FROM Photo WHERE test = '"+tab[1]+"' AND horaire = '"+tab[2]+"'"
		select_request = "SELECT ID FROM Photo WHERE test = '"+tab[1]+"' AND horaire = '"+tab[2]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"

	elif tab[1] != 'Null' and tab[2] != 'Null' and tab[3] != 'Null':
		delete_request = "DELETE FROM Photo WHERE test = '"+tab[1]+"' AND horaire = '"+tab[2]+"' AND date = '"+tab[3]+"'"
		select_request = "SELECT ID FROM Photo WHERE test = '"+tab[1]+"' AND horaire = '"+tab[2]+"' AND date = '"+tab[3]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"

	elif tab[1] == 'Null' and tab[2] != 'Null' and tab[3] != 'Null':
		delete_request = "DELETE FROM Photo WHERE horaire = '"+tab[2]+"' AND date = '"+tab[3]+"'"
		select_request = "SELECT ID FROM Photo WHERE horaire = '"+tab[2]+"' AND date = '"+tab[3]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"

	elif tab[1] == 'Null' and tab[2] != 'Null' and tab[3] == 'Null':
		delete_request = "DELETE FROM Photo WHERE horaire = '"+tab[2]+"'"
		select_request = "SELECT ID FROM Photo WHERE horaire = '"+tab[2]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"

	elif tab[1] == 'Null' and tab[2] == 'Null' and tab[3] != 'Null':
		delete_request = "DELETE FROM Photo WHERE date = '"+tab[3]+"'"
		select_request = "SELECT ID FROM Photo WHERE date = '"+tab[3]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"
	elif tab[1] != 'Null' and tab[2] == 'Null' and tab[3] != 'Null':
		delete_request = "DELETE FROM Photo WHERE test = '"+tab[1]+"' AND date = '"+tab[3]+"'"
		select_request = "SELECT ID FROM Photo WHERE test = '"+tab[1]+"' AND date = '"+tab[3]+"'"
		try:
			the_cursor.execute(select_request)
			res = the_cursor.fetchall()
			mariadb_connection.commit()
			for i in res:
				os.remove('/var/www/html/tools/image/'+str(i[0])+'.png')
			the_cursor.execute(delete_request)
			mariadb_connection.commit()
			return ' supprimer avec succès !'
		except:
			return "ERROR"






##### ADD #####

def add( nom, prenom, secret, role, the_cursor, user):
	#récupération des variables
	ident = identif( nom, prenom)
    date = strftime(%Y-%m-%d %H:%M:%S, datetime.now())
	if nom == "error" and prenom == "error":
		return "ERROR"
    with open("log.txt", "w") as file:
        file.write(user + " a un utilisateur le " + date +".")

	#création de la ligne SQL
	insert_request = 'INSERT INTO Users VALUES (%s,%s,%s)'

	#ajouter un compte à la table
	try:
		the_cursor.execute(insert_request, (ident, secret, role))
		mariadb_connection.commit()
		return ident
	except:
		nb = 1
		try:
			the_cursor.execute(insert_request, (ident + str(nb), secret, role))
			mariadb_connection.commit()
			return ident
		except:
			nb = nb + 1
			try:
				the_cursor.execute(insert_request, (ident + str(nb), secret, role))
				mariadb_connection.commit()
				return ident
			except:
				nb = nb + 1
				try:
					the_cursor.execute(insert_request, (ident + str(nb), secret, role))
					mariadb_connection.commit()
					return ident
				except:
					nb = nb + 1
					try:
						the_cursor.execute(insert_request, (ident + str(nb), secret, role))
						mariadb_connection.commit()
						return ident
					except:
						nb = nb + 1
						try:
							the_cursor.execute(insert_request, (ident + str(nb), secret, role))
							mariadb_connection.commit()
							return ident
						except:
							nb = nb + 1
							try:
								the_cursor.execute(insert_request, (ident + str(nb), secret, role))
								mariadb_connection.commit()
								return ident
							except:
								nb = nb + 1
								try:
									the_cursor.execute(insert_request, (ident + str(nb), secret, role))
									mariadb_connection.commit()
									return ident
								except:
									nb = nb + 1
									try:
										the_cursor.execute(insert_request, (ident + str(nb), secret, role))
										mariadb_connection.commit()
										return ident
									except:
										nb = nb + 1
										try:
											the_cursor.execute(insert_request, (ident + str(nb), secret, role))
											mariadb_connection.commit()
											return ident
										except:
											return "ERROR"




#### SUPP ####

def supp(ident, the_cursor, user):
	delete_request = "DELETE FROM Users WHERE ID = '"+ident+"'"
    date = strftime(%Y-%m-%d %H:%M:%S, datetime.now())
    with open("log.txt", "w") as file:
            file.write(user + " a supprimé l'utilisateur "+str(ident)+" le " + date +".")
	try:
		the_cursor.execute(delete_request)
		mariadb_connection.commit()
		return ident + ' supprimer avec succès !'
	except:
		return "ERROR"






#### DELTABLE ####

def deltable(table, the_cursor, user):
	delete_request = "DROP TABLE "+table
	try:
		the_cursor.execute(delete_request)
		mariadb_connection.commit()
		return "SUCCES"
	except:
		return "ERROR"



#### SEARCH ####

def search(ident, mdp, the_cursor):
	select_request = "SELECT * FROM Users WHERE ID = '"+ident+"'"
	try:
		the_cursor.execute(select_request)
		res = the_cursor.fetchall()
		if res[0][0] == ident and res[0][1] == mdp:
			return res[0][2]
		else:
			return "FAILED"
	except:
		return "ERROR"



def affichetable():
	the_cursor.execute("SHOW TABLES")
	syntaxe = "TABLES: \n"
	for x in the_cursor:
		syntaxe = syntaxe + str(x) +'\n'

	syntaxe = syntaxe + "\n Users: \n"
	the_cursor.execute("SELECT * FROM Users")
	for x in the_cursor:
		syntaxe = syntaxe + str(x) +'\n'

	syntaxe = syntaxe + "\n Photo: \n"
	the_cursor.execute("SELECT * FROM Photo")
	for x in the_cursor:
		syntaxe = syntaxe + str(x) +'\n'
	return syntaxe









#création d'une connection
mariadb_connection = mariadb.connect(user='root', password='root', host='localhost', port='3306')


#création d'un curseur
the_cursor = mariadb_connection.cursor()





############ CREATION BASE DE DONNEES & TABLES ############

#créer la BD
the_cursor.execute("CREATE DATABASE IF NOT EXISTS UsersDB")

#mettre à jour la connection
mariadb_connection = mariadb.connect(user='root', password='root', database='UsersDB', host='localhost', port='3306')
the_cursor = mariadb_connection.cursor()





#créer les tables
the_cursor.execute("CREATE TABLE IF NOT EXISTS Users (ID varchar(50) NOT NULL, mdp varchar(50), role varchar(5), PRIMARY KEY(ID))")
the_cursor.execute("CREATE TABLE IF NOT EXISTS Photo (ID INT NOT NULL AUTO_INCREMENT, test varchar(50), chemin varchar(50), user varchar(20), date varchar(25), PRIMARY KEY(ID))")








################################################################################################# AJOUTER DES USERS ######################################################################################



result = "..."


################################################################################################ CHOIX DE LA FONCTION ##########################################################################################

if sys.argv[1] == "add":
	result = add(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5], the_cursor, sys.argv[6])
elif sys.argv[1] == "supp":
	result = supp(sys.argv[2], the_cursor, sys.argv[3])
elif sys.argv[1] == "deltable":
	result = deltable(sys.argv[2], the_cursor)
elif sys.argv[1] == "search":
	result = search(sys.argv[2],sys.argv[3], the_cursor)
elif sys.argv[1] == "affichetable":
	result = affichetable()
elif sys.argv[1] == "photo":
	result = photo(sys.argv[2],sys.argv[3],the_cursor)
elif sys.argv[1] == "suppPho":
	tab = [sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]]
	result = suppPhoto(tab, the_cursor)





#the_cursor.execute("SHOW TABLES")
#for x in the_cursor:
	#print(x)

#the_cursor.execute("SELECT * FROM Users")
#for x in the_cursor:
	#print(x)

print(result)
