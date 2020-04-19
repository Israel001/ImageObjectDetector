try:
    import urllib.request
    from http.cookiejar import CookieJar
except ImportError:
    import urllib2
    from urllib2 import urlopen
    from cookielib import CookieJar
import re
from flask import Flask, jsonify, request

app = Flask(__name__)
cj = CookieJar()
try:
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
except:
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Israel\'s Simple Image Object Identifier API Landing Page. Please visit /imagelookup/your_img to detect the image object. Thank you'

@app.route('/imagelookup', methods=['GET'])
def imageLookUp():
    imagepath = request.args.get('image')
    
    googlepath = 'http://images.google.com/searchbyimage?image_url='+imagepath

    sourceCode = opener.open(googlepath).read().decode('utf-8')

    regex = r'<input class="gLFyf gsfi"(.*?)>' 

    pattern = re.compile(regex)

    findElement = re.findall(pattern, sourceCode)

    for eachElement in findElement:
        validEl = eachElement
        
    newregex = r'value="(.*?)"'

    newpattern = re.compile(newregex)

    extractName = re.findall(newpattern, validEl)

    return jsonify({'imgObj': extractName})

if __name__ == '__main__':
    app.run(debug=True)

