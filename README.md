# YDiskTask

Проект взаимодействует с диском по API. Предоставляет возможность перехода в папки и скачивания файлов.

![Python](https://img.shields.io/badge/Python-3.12-blue)

## Установка
1. Клонируйте репозиторий  
```sh
git clone https://github.com/Skro11X/YDiskTask
```
2. Установите python версии 3.12
   
   Windows:
   
   https://www.python.org/downloads/release/python-3128/
   
   Ubuntu:

```shell
sudo apt-get install python3.11
```

3. Создайте виртуальное окружение питона и активируйте его и скачайте зависимости.

Windows
```shell
python -m venv venv
venv\Scripts\activate
pip install -r pip install -r requirements.txt
 ```

Ubuntu
```shell
python -m venv venv
source venv/bin/activate
pip install -r pip install -r requirements.txt
```

4. Запустить дефолтный сервер Django
```shell
python manage.py runserver
```


---
На задачу ушло в общем 19 часов.

Основная логика и верстка была выполнена за 8 часов. Речь идет об обращении к апи и отображении информации верхнего уровня диска и предоставлении возможности скачивания информации с диска.

Далее оптимизировал страницу тем что предоставил эндпоинт по формированию ссылки на скачивание по нажатию на кнопку.(3 часа)

После реализовывал возможность переключаться между папками.(3 часа)

В течении выходных займусь реализацией функций указанных в тестовом задании как дополнительные. 

Добавил возможность фильтрации и улучшил визуальную составляющую сайта. (5 часов)
