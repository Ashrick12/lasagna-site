from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            like = request.form.get('like')
            name = request.form.get('name')
            frozen = request.form.get('frozen')
            with open('opinions.csv', 'a') as f:
                f.write(f'\n{name},{like},{frozen}')
        except:
            print('Error Occured, probably fine.')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)