from flask import Flask,jsonify,make_response,render_template
from api import api_bp


app=Flask(__name__,static_folder='./static')
app.register_blueprint(api_bp,url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True)