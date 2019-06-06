from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def webpage():
    return render_template('webpage.html')

@app.route('/', methods=['POST'])
def web_url():
    url = request.form['url']
    processed_url = url.lower()
    urlcheck = requests.get(processed_url)
    #print(urlcheck.status_code)
    code = urlcheck.status_code
    return render_template('webpage.html', url = processed_url,  status=code)

if __name__=='__main__':
    app.run(host='0.0.0.0')
#    statuscheck(processed_url)

#def statuscheck(url_check):
#    request = requests.get(url_check)
#    print(request.status_code)

