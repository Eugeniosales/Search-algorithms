from flask import Flask, render_template,request, jsonify, json
from methods.switch_method import switch_method

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():

    searchMeth1 = []
    searchMeth2 = []
    max = 0
    key = 0
    value = []

    if request.method == 'POST':
        
        forms = {
            'first': request.form['primeiraBusca'], 
            'second': request.form['segundaBusca'],
            'max': request.form['max'],
            'key': request.form['key']
        }

        max = int(forms['max'])
        key = int(forms['key'])

        searchMeth1 = forms['first']
        searchMeth2 = forms['second']

        if key>max:
            key = -1
            max = -1
            value = [-1,-1]
            return render_template("index.html", value=json.dumps(value), searchMeth1=searchMeth1, searchMeth2=searchMeth2, max=json.dumps(max), key=json.dumps(key))


        steps1 = switch_method(forms['first'], max, key)
        steps2 = switch_method(forms['second'], max, key)
        
        value.append(steps1)
        value.append(steps2)

        

        return render_template("index.html", value=json.dumps(value), searchMeth1=searchMeth1, searchMeth2=searchMeth2, max=json.dumps(max), key=json.dumps(key))
    
    return render_template("index.html", value=json.dumps(value), searchMeth1=searchMeth1, searchMeth2=searchMeth2, max=json.dumps(max), key=json.dumps(key))


if __name__ == '__main__':
    app.run(debug=True)