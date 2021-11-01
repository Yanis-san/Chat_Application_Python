# coding: utf-8

import cgi
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yanisb",
    database="pravan"
    )
cursor = conn.cursor()

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print()

html = """<!DOCTYPE html>
<head>
    <title>BPChat</title>
    <link rel="stylesheet" href= "/media/style.css">
</head>
<body>
    <h1>Blackpink Chat</h1>
    <div class="container">
        <form action="index.py" method="post">
            <p class="titre">Pseudo </p> <input type="text" name="pseudo" id=" pseudo" placeholder="Entrez votre pseudo" required/>
            <p class="titre">Message </p><textarea placeholder="Entrez votre message" name="message" id="msg" required></textarea> </br>
            <input type="submit" name="send" value="Envoyer" id="valid">
        </form>  
</body>
</html>
"""

print(html)

cursor.execute("SELECT pseudo,message FROM ( SELECT * FROM message ORDER BY id DESC LIMIT 10) sub ORDER BY id ASC")
result = cursor.fetchall()
print("""<ul><br/>""")
for row in result:
    print("""<li><span class="psd">""")
    print(row[0])
    print(""":</span>""")
    print(row[1])
    print("""</li>""")
print("""</ul></div><p id="copyright">&copy; 2021 Yanis Barbara</p></body>
</html>""")
conn.close()