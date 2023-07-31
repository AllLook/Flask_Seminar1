from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('base.html')


@app.route('/outerwear/')
def outerwear():
    jackets = {'Black': 'Size 48: black jackets', 'Blue': 'Size 50: blue jackets', 'Yellow': 'Size 52: yellow jackets',
               'White': 'Size 54: white jackets'}
    return render_template('outerwear.html', jackets=jackets)


@app.route('/Summer/')
def summer():
    clothing = {'Black': 'Size 48: black T-shirt', 'Blue': 'Size 50: blue T-shirt', 'Yellow': 'Size 52: yellow shorts',
                'White': 'Size 54: white shorts'}
    return render_template('Summer.html', clothing=clothing)


@app.route('/dresses/')
def dresses():
    dres = {'Black': 'Size 48: black dresses', 'Blue': 'Size 50: blue dresses', 'Yellow': 'Size 52: yellow dresses',
            'White': 'Size 54: white dresses'}
    return render_template('dresses.html', dres=dres)


if __name__ == '__main__':
    app.run()
