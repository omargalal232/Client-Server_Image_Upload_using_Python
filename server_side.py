from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__)

cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'localhost:9199',
    'databaseURL': 'http://localhost:8080'
})

@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        uploaded_image = request.files['image']

        bucket = storage.bucket()
        blob = bucket.blob('images/' + uploaded_image.filename)
        blob.upload_from_file(uploaded_image)

        return "Image successfully uploaded to Firebase Storage", 200

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
