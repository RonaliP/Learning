from flask import Flask,redirect,url_for,render_template

app = Flask(__name__,template_folder="templates")


@app.route("/")
def home():
    return render_template( "index.html",content="TESTING" )

if __name__ == "__main__":
    app.run(debug=True)


    