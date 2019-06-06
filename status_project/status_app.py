from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# If the user comes on / path, it gets redirected to webpage.html saved under /templates directory.

@app.route('/')
def webpage():
    return render_template('webpage.html')

# render_template will render and display the specified html page.

@app.route('/', methods=['POST'])
def web_url():
    url = request.form['url']
    processed_url = url.lower()
    urlcheck = requests.get(processed_url)
    # requests.get will perform an GET request to specified URL and fetch the response code.
    #print(urlcheck.status_code)
    code = urlcheck.status_code
    # status_code displays the http response code from requests.get method
    return render_template('webpage.html', url = processed_url,  status=code)#render_template is passed with some values that are written as variables in html file


if __name__=='__main__':
    app.run() # runs the flask app and starts listening on localhost:5000

