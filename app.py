from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['GET'])
def callback():
    # handle the callback here
    return 'Callback handled'

if __name__ == '__main__':
    PORT = 3000
    app.run(port=PORT, debug=True)
