import pycouchdb

def create_member():
	global db
	global doc
	server = pycouchdb.Server("http://nation:oleoleole@localhost:5981/")
	db = server.database("members")
	doc = db.save(
		{
			"kind": "Member",
		   "roles": [
			   "Learner"
		   ],
		   "bellLanguage": "English",
		   "firstName": "q",
		   "lastName": "q",
		   "middleNames": "q",
		   "login": "q",
		   "password": "",
		   "phone": "q",
		   "email": "q",
		   "language": "q",
		   "BirthDate": "1915-12-31T22:00:00.000Z",
		   "visits": 0,
		   "Gender": "Male",
		   "levels": "1",
		   "status": "active",
		   "community": "NATION",
		   "region": "",
		   "nation": "earthbell",
		   "lastLoginDate": "2016-12-15T22:00:00.000Z",
		   "lastEditDate": "2016-12-16T14:48:32.771Z",
		   "credentials": {
			   "salt": "7694f4a66316e53c8cdd9d9954bd611d",
			   "value": "5605c1a22a715e2cb1966a1f4e244e87588c385c",
			   "login": "q"
		   }
		}
    	)  

def delete_member():
	db.delete(doc)


