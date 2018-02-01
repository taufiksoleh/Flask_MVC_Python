from flask import request, json, render_template
from werkzeug.security import generate_password_hash

from app import app
from app.models.user_model import user_model


@app.route('/',methods=['GET'])
def main_world():
    return render_template('static/index.html')

@app.route('/insert',methods=['POST'])
def insert():
    # read request from UI
    _name   = request.form['username']
    _email  = request.form['email']
    _pass   = request.form['password']
    _hash_pass = generate_password_hash(_pass)

    if _name and _email and _pass:
        user = user_model()
        result = user.insert(_name,_email,_hash_pass)
        if(result):
            return json.dumps({'html':'<span>Data Inserted </span>'})
        else:
            return json.dumps({'html':'<span>Inserted Failed </span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/show')
def show():
    user = user_model()
    data = user.get_user()
    data_list = []
    if data is not None:
        for item in data:
            data_temp_obj = {
                'id'        : item[0],
                'name'      : item[1],
                'email'     : item[2],
                'password'  : item[3]
            }
            data_list.append(data_temp_obj)
        return json.dumps(data_list)
    else:
        return 'data kosong'

@app.route('/update/<id>',methods=['POST'])
def update(id):
    _name   = request.form['username']
    _email  = request.form['email']
    _pass   = request.form['password']

    user = user_model()
    result = user.update(id,_name,_email,_pass)
    if(result):
        return json.dumps({'updated':'true'})
    else:
        return json.dumps({'updated':'false'})

@app.route('/delete/<id>')
def delete(id):
    user = user_model()
    result = user.delete(id)
    if(result):
        return json.dumps({'delete':'true'})
    else:
        return json.dumps({'delete':'false'})
