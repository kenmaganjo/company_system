from flask import Flask, render_template
import psycopg2
app = Flask(__name__)
conn = psycopg2.connect(user="postgres", password="1958",
 host="localhost", port="5432", database="gift_shop")

cur=conn.cursor()


@app.route('/')
def hello_world():
    name="ken"
    
    return render_template("index.html",name=name)

@app.route('/sales')
def sales():
    cur.execute("select * from sales;")
    sales = cur.fetchall()
    print(sales)
  

    return render_template("sales.html",sales=sales)


if __name__ == "__main__":
    app.run()