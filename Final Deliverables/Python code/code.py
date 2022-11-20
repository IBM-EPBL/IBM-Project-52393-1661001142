from flask import Flask, render_template
app = Flask( name )
@app.route("/")
def bot():
    return render_template('Chatbot.html')
if name == ' __main ':
    app.run()
