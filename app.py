from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
    con = sqlite3.connect('books.db')
    return con

@app.route("/books", methods=['GET', 'POST'])
def getAndCreateBooks():
    con = db_connection()
    cursor = con.cursor()

    if request.method == 'GET':
        cursor = con.execute("SELECT * FROM Book")
        books = []
        res = cursor.fetchall()
        for row in res:
            book = {'id':row[0],'author':row[1],
            'language':row[2],'title':row[3]}
            books.append(book)
        return jsonify(books)

    if request.method == 'POST':
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        cursor = con.execute("INSERT INTO Book (author, language, title) values (?,?,?)", (author,language, title))
        con.commit()
        return "Book created successfully"



@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def getAndUpdateAndDeleteBooks(id):
    con = db_connection()
    cursor = con.cursor()

    if request.method == "GET":
        sql = cursor.execute("Select * from Book where id = ?", (id,))
        book = cursor.fetchall()
        for row in book:
            res = {'id':row[0],'author':row[1],
            'language':row[2],'title':row[3]}
        return jsonify(res)
    elif request.method == "PUT":
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        cursor = con.execute("UPDATE Book SET author = ? where id = ?",(author, id))
        con.commit()
        return "Book updated successfully"
    else:
        cursor = con.execute("DELETE FROM Book where id = ?", (id,))
        return "Book Deleted"

if __name__ == "__main__":
    app.run()
