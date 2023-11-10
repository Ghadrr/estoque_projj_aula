"""
WSGI config for _nome_do_projetoestoque_projj_aula project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_nome_do_projetoestoque_projj_aula.settings')

application = get_wsgi_application()
