import requests
from PIL import Image
from io import BytesIO

def download_and_show_cat():
    """
    Скачивает случайное изображение кота и отображает его
    """
    try:
        # URL API для получения случайного изображения кота
        url = "https://cataas.com/cat"
        
        print("Скачиваю изображение кота...")
        
        # Скачиваем изображение
        response = requests.get(url)
        response.raise_for_status()  # Проверяем на ошибки
        
        # Открываем изображение из полученных данных
        img = Image.open(BytesIO(response.content))
        
        print("Изображение успешно загружено!")
        
        # Отображаем изображение
        img.show()
        
        # Сохраняем изображение на диск
        filename = "кот.jpg"
        img.save(filename)
        print(f"Изображение сохранено как: {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при скачивании: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    download_and_show_cat()
