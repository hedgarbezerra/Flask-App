import configparser
import os
import random
import string

# Armazena a localização atual do arquivo
basedir = os.path.dirname(os.path.realpath(__file__))

# Ler as configurações do banco de um arquivo
config = configparser.ConfigParser()
config.read(f'{basedir}/config.ini')
user = config['DATABASE']['user']
passwd = config['DATABASE']['passwd']
dbc = config['DATABASE']['db']
host = config['DATABASE']['host']
port = int(config['DATABASE']['port'])

# Gera uma chave aleatória para aplicação a cada execução do servidor
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))

# Definições do banco de dados e app
SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{passwd}@{host}:{port}/{dbc}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
DEBUG = True
