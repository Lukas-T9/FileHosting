from flask import Flask, request, jsonify, send_file
import requests
import io
import os
import datetime

app = Flask(__name__)

globalUrl = "https://file.run-eu-central1.goorm.app"
MAX_FILE_STORAGE_DAYS = 14


def get_deletion_date():
    current_date = datetime.datetime.now()
    deletion_date = current_date + datetime.timedelta(days=MAX_FILE_STORAGE_DAYS)
    return deletion_date


@app.route('/download')
def download_file():
    # Получаем имя файла из параметра запроса
    filename = request.args.get('filename')
    if not filename:
        return "Имя файла не указано"
    
    transfer_url = f"https://transfer.sh/get/{filename}"
    
    response = requests.get(transfer_url)
    if response.status_code == 200:
        file_content = response.content
        # Отправляем файл пользователю с указанием имени для скачивания
        return send_file(io.BytesIO(file_content), as_attachment=True, attachment_filename=filename)
    else:
        return "Ошибка при загрузке файла"



@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    if file:
        filename = file.filename

        url = "https://transfer.sh/"
        files = {"file": (filename, file)}
        response = requests.post(url, files=files)

        download_url = response.text.strip().replace(url, f"{globalUrl}/download?filename=")
        deletion_date = get_deletion_date().strftime('%Y-%m-%d')
        return jsonify({"url": download_url, 'deletion_date': deletion_date}), 200

    else:
        return jsonify({"error": "Файл не загружен"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
