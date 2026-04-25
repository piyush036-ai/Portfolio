from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__)


@app.route('/profile.jpeg')
def profile_image():
    return send_from_directory(app.root_path, 'profile.jpeg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    # In production, integrate with email service
    return jsonify({'status': 'success', 'message': 'Message received!'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
