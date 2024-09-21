from importlib import import_module
import os
import grpc
from concurrent import futures
import settings
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


def add_servicer_to_server(server):
    path = os.path.realpath(os.path.dirname(__file__))
    for module_name in os.listdir(f'{path}/service'):
        module = import_module(f'service.{module_name}.servicer')
        module.add_servicer_to_server(server)


if __name__ == '__main__':
    logging.info(f'creating grpc server: {settings.host}:{settings.port}...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_servicer_to_server(server)
    server.add_insecure_port(f'{settings.host}:{settings.port}')

    logging.info('starting server...')
    server.start()
    server.wait_for_termination()
