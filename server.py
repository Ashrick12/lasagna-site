from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            like = request.form.get('like')
            name = request.form.get('name')
            opinion = (name, like)
            with open('opinions.txt', 'a') as f:
                f.write(f'\n{opinion}')
        except:
            print('Error Occured, probably fine.')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)