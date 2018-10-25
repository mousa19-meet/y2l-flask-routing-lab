from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/shop')
def shop_page():
	return render_template('shop.html')

if __name__ == '__main__':
   app.run(debug = True)
