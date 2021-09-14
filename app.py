from flask import Flask

app = Flask('__name__')

@app.route('/')
def home():
    return 'welcome to cognitivzen technologys'

@app.route('/getusers')
def getusers():
    return 'There are no users..........'


if '__name__' = '__main__':
    
    app.run(debug=True)