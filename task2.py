
import json
import requests

FILES_URL = "https://cloud-api.yandex.net/v1/disk/resources/files"
UPLOAD_URL = "https://cloud-api.yandex.net/v1/disk/resources/upload"


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }

    def get_files_list(self):
        """Метод возвращает список файлов на яндекс диске"""
        headers = self.get_headers()
        response = requests.get(FILES_URL, headers=headers)
        #        print(response.json())
        return response.json()

    def _get_upload_link(self, file_name):
        """Метод возвращает ссылку для загрузки файла"""
        headers = self.get_headers()
        params = {"path": file_name, "overwrite": "true"}
        response = requests.get(UPLOAD_URL, headers=headers, params=params)
        if response.status_code == 200:
            print("URL для загрузки файла получен успешно")
        else:
            print("Ошибка, status code: " + str(response))
        return (response.json())

    def upload(self, file_name):
        """Метод загружает файл по имени file_name на яндекс диск"""
        href = self._get_upload_link(file_name=file_name).get("href", "")
        if not href:
            return "Oшибка: href == None"
        #        print("href:", href)
        response = requests.put(href, data=open(file_name, "rb"))
        if response.status_code == 201:
            return "Файл загружен успешно"
        return "Ошибка, status code: " + str(response)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_name = input("Введите имя файла для загрузки: ")
    token = input("Введите токен от Yandex-Диска: ")

    # Загрузить файл на Яндекс-Диск
    uploader = YaUploader(token)
    print(uploader.upload(file_name))