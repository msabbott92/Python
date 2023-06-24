from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/')          
def hello_flask():
    return render_template("index.html")
    
@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return render_template("hello.html",banana=banana, num=num)

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output



if __name__=="__main__":     
    app.run(debug=True)    

