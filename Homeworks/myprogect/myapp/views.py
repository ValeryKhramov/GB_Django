from django.http import HttpResponse



def main(request):
    html_main = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            div {
                margin-left: 600px;
                margin-right: 600px;
            }


        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
         <nav>
            <button><a href='index'>Главная</a></button>
            <button><a href='about'>О себе</a></button>
         </nav>
    </body>
    </html>
    """
    return HttpResponse(html_main)


def about_me(request):
    html_about = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            div {
                margin-left: 600px;
                margin-right: 600px;
            }


        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>

        <h2>Обо мне</h2>
        <div>
            <p>Меня зовут Валерий, мне 23 года, являюсь начинающим Python разработчиком.</p>
         </div>
         <nav>
            <dl>
                <button><a onclick="javascript:history.back(); return false;">Назад</a></button>
            </dl>
         </nav>
    </body>
    </html>
    """
    return HttpResponse(html_about)


def index(request):
    html_index = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            div {
                margin-left: 600px;
                margin-right: 600px;
            }


        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>

        <h2>О сайте</h2>
        <div>
            <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке 
            Python. Здесь я могу создавать и отображать различные страницы и данные в удобном формате.</p>
         </div>
         <nav>
           
            <button><a onclick="javascript:history.back(); return false;">Назад</a></button>
            
         </nav>
    </body>
    </html>
    """
    return HttpResponse(html_index)
