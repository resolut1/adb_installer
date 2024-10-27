
import requests
from apk_links import app_links_dict
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}


for app in app_links_dict:
    url = app_links_dict[app]
    try:
        response = requests.get(url, headers=headers, stream=True)

        if response.status_code == 200:
            with open(f'apps_apk/{app}', 'wb') as apk_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        apk_file.write(chunk)

            print(f"Файл успешно скачан и сохранен как {app}")
        else:
            print(f"Не удалось скачать файл. Статус: {response.status_code}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

print('[INFO] Обновление закончено!')
