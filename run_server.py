import os
import sys
from waitress import serve
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler # ou WSGIHandler alternativo

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_painel_baxter.settings')

application = get_wsgi_application()

# Importação para forçar o envio de estáticos em produção pelo script
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(application)

if __name__ == '__main__':
    print("Iniciando servidor Waitress na porta 8000...")
    serve(application, host='127.0.0.1', port=8000, threads=1)