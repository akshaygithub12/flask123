from flask import Flask, redirect, url_for, request

app=Flask(__name__)
@app.route('/new',methods=["get","post"])
def post():
    if request.method=="post":
        post_name=request.form['name']
        post_age=request.form['age']
        return redirect(url_for('success',name = post_name))
if __name__=='__main__':
    app.run(debug=True)

    
