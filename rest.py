from flask import (
    Flask,
    render_template
)
import connexion
from connexion.resolver import RestyResolver
from flask_cors import CORS

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the yaml file to configure the endpoints
app.add_api('openapi.yaml')
CORS(app.app)

# Create a URL route in our application for "/"
@app.route('/ui')
def home():
    """
    This function just responds to the browser ULR
    anyhost:5001/
    :return:        the rendered template 'home.html'
    """
    return render_template('index.html')
    
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('openapi.yaml')

# Create a URL route in our application for "/"
@app.route('/ui')
def home():
    """
    This function just responds to the browser ULR
    anyhost:5001/
    :return:        the rendered template 'home.html'
    """
    return render_template('index.html')


from OpenSSL import SSL

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)