from flask import Flask, request, render_template
import requests
from requests.exceptions import ConnectionError, MissingSchema

app = Flask(__name__)

@app.route('/') #If the user comes on /path, it gets redirected to webpage.htm saved under templates directory

def webpage():
    return render_template('webpage.html')# render_template will render and display the specified html page

@app.route('/', methods=['POST'])
def web_url():
    url = request.form['url']
    processed_url = url.lower()
    try:
        urlcheck = requests.get(processed_url)
        code = urlcheck.status_code
        return render_template('webpage.html', url = processed_url,  status=code)
    except ConnectionError:
        return render_template('webpage.html', url = processed_url, status = 'The website does not exist')
    except MissingSchema:
        return render_template('webpage.html', url = processed_url, status = 'The URL format is incorrect. Please try again!')

if __name__=='__main__':
    app.run(host='0.0.0.0')
#    statuscheck(processed_url)

#def statuscheck(url_check):
#    request = requests.get(url_check)
#    print(request.status_code)

