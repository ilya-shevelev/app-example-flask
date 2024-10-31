from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/src/main.ts')
def get_main_ts():
    return send_from_directory(directory='src', path='main.ts')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)