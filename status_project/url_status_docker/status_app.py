from flask import Flask, request, render_template
import requests
from requests.exceptions import ConnectionError, MissingSchema
import time

app = Flask(__name__)
url_dict = {}
@app.route('/') #If the user comes on /path, it gets redirected to webpage.htm saved under templates directory

def webpage():
    return render_template('webpage.html')# render_template will render and display the specified html page

@app.route('/', methods=['POST'])
def web_url():
    url = request.form['url']
    processed_url = url.lower()
    try:
        if processed_url in url_dict:
            if url_dict[processed_url][0]- int(time.time()) > 600:
                urlcheck = requests.get(processed_url)
                code = urlcheck.status_code
                url_dict[processed_url] = [int(time.time()), code]
                if code == 200:
                    return render_template('webpage.html', url = processed_url,  status=code, availability = 'The website you specified is availble!', cache = url_dict.items())
                else:
                    return render_template('webpage.html', url = processed_url, status=code,
                                   availability = 'The website you specified returned {}!'.format(code), cache = url_dict.keys())
            else:
                return render_template('webpage.html', url = processed_url, status=url_dict[processed_url][1], availability = 'As in dict, yet to add', cache = url_dict.keys())
        else:
            urlcheck = requests.get(processed_url)
            code = urlcheck.status_code
            url_dict[url] = [int(time.time()), code]
            if code == 200:
                return render_template('webpage.html', url = processed_url,  status=code, availability = 'The website you specified is availble!', cache = url_dict.items())
            else:
                return render_template('webpage.html', url = processed_url, status=code,
                                       availability = 'The website you specified returned {}!'.format(code), cache = url_dict.keys())
        
    except ConnectionError:
        return render_template('webpage.html', url = processed_url, status = 'The website does not exist')
    except MissingSchema:
        return render_template('webpage.html', url = processed_url, status = 'The URL format is incorrect. Please try again!')

if __name__=='__main__':
    app.run(host='0.0.0.0')

