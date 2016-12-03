


from flask import Flask, request, render_template
app = Flask(__name__)  

@app.route("/")
def root():
    return app.send_static_file('index.html')


@app.route("/about")
@app.route('/about/<name>')
def about(name=None):
    return render_template('about.html', name = name)

	
	
@app.route("/gallery/")
def gallery(name=None):
    return render_template('gallery.html', name = name)
	
	
@app.route("/contact/")
def poll(name=None):
	return render_template('contact.html', name = name)
	
if __name__ == "__main__":     
	app.run()
