# config.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cakd7_erp',
        'USER': 'root',
        'PASSWORD': '12345678',  # mysql root 유저 비밀번호 입력
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
