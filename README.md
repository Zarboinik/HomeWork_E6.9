# HomeWork_E6.9

1 git clone https://github.com/Zarboinik/HomeWork_E6.9.git

2 Создать вертуальное окружение в проекте( для pycharm -> settings -> Название проекта -> Python Interpreter -> Add Interpreter)

3 venv/scripts/activate

4 cd backend

5 python manage.py migrate

6 в отдельно терменале docker run --rm -p 6379:6379 redis:7

7 py manage.py runserver


если ругнётся установите ещё Pillow 
python -m pip install Pillow
