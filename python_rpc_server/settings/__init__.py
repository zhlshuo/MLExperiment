import os
import importlib

region = os.getenv('REGION', 'us')
env = os.getenv('ENV', 'dev')

setting = importlib.import_module(f'settings.{region}.{env}')
for attr in dir(setting):
    if not attr.startswith('__'):
        globals()[attr] = getattr(setting, attr)
