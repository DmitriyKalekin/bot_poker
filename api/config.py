import os

class BaseConfig:
    DEBUG = False
    TESTING = True
    CFG_ENV = "staging"
    
    # MySQL
    # MYSQL_USER = os.getenv('MYSQL_USER')
    # MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    # MYSQL_HOST = os.getenv('MYSQL_HOST')
    # MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    # MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123123"
    MYSQL_HOST = "localhost"
    MYSQL_PORT = 3306
    MYSQL_DATABASE = "bot_poker" 

    # www
    CFG_WWW = "127.0.0.1" # 139.59.142.122

    CFG_CERT     = '/root/cert.pem'
    CFG_CERT_KEY = '/root/private.key' 

     # Telegram
    CFG_TELEGRAM_KEY    = '676006235:AAHPUUY5EvJoU7xT1EhRbMkR91byXNCR3KI'
    CFG_PORT     = 5001 #443
    CFG_TELEGRAM_API_URL = f'https://api.telegram.org/bot{CFG_TELEGRAM_KEY}/'
    CFG_SERVICE_WEBHOOK_URL = f'https://{CFG_WWW}/'

    CFG_LOCALHOST = "0.0.0.0"
    CFG_SSL_CONTEXT = (CFG_CERT, CFG_CERT_KEY)
    CFG_SSL_CONTEXT = None
    CFG_DEBUG = True
 





class Production(BaseConfig):
    DEBUG = False


class Staging(BaseConfig):
    DEBUG = True


class Development(BaseConfig):
    DEBUG = True

cfg = Staging()    
    
