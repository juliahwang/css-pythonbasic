from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
	return "First Flask Application!!"

@app.route('/index')
def render(name=None):
	return render_template("index.html", name=name)

@app.route('/about_render')
def about(name=None):
	return render_template("about.html", name=name)


if __name__ == '__main__':
	app.run(host = '0.0.0.0')
