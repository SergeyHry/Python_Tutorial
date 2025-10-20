import csv
import matplotlib.pyplot as plt
from flask import Flask, render_template,url_for, request
from flask_mysqldb import MySQL

from lists import alter

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1111'
app.config['MYSQL_DB'] = 'bookstore'
app.config['MYSQL_PORT'] = 3307
mysql = MySQL(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index/post', methods=['GET', 'POST'])
def index_pos():
    if request.method == 'POST':
        title = request.form['title']
        firstname = request.form.get('firstName')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        city = request.form.get('city')
        address = request.form.get('address')
        age = request.form.get('age')
        age2 = alter(age)
        cur = mysql.connection.cursor()
        cur.execute("""
                    INSERT INTO customers (title, firstname, lastname, email, city, street, age)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (title, firstname, lastname, email, city, address, age2))
        mysql.connection.commit()
        cur.close()

        return "✅ Daten erfolgreich gespeichert!"
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/customers')
def customers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customers")
    users = cur.fetchall()
    cur.close()

    page = request.args.get('page', 1, type=int)
    per_page = 20

    start = (page - 1) * per_page
    end = start + per_page
    paginated_users = users[start:end]
    total_pages = (len(users) + per_page - 1) // per_page
    return render_template('customers.html', users= paginated_users, page=page, total_pages=total_pages)

@app.route('/writeCsv')
def writeCsv():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customers LIMIT 20")
    users = cur.fetchall()
    cur.close()
    filepath = 'C:/Users/Student/Desktop/bookstore.csv'
    with open (filepath, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Optional: Kopfzeile
        writer.writerow(['ID', 'First Name', 'Last Name', 'Street', 'City', 'Email', 'Age'])

        for user in users:
            writer.writerow(user)

    return f'Datei gespeichert unter: {filepath}'


if __name__ == '__main__':
    app.run(debug=True)