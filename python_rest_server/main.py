import grpc
from protoc.hello_pb2_grpc import HelloStub
from protoc.hello_pb2 import HelloRequest
from flask import Flask
import flask_profiler
from flask_cors import CORS
import importlib
import os
import settings

app = Flask(__name__)
CORS(app)
app.config['flask_profiler'] = {
    "enabled": settings.PROFILER_ENABLED,
    "storage": {
        "engine": "sqlalchemy"
    }
}

flask_profiler.init_app(app)


def register_urlpatterns(app):
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    servicePath = os.path.join(scriptPath, "service")
    for serviceModuleName in os.listdir(servicePath):
        serviceModule = importlib.import_module(
            f'service.{serviceModuleName}.endpoint')
        for rule, view_func, options in serviceModule.get_url_patterns():
            view_name = f'{serviceModuleName}.{view_func.__name__}'
            app.add_url_rule(rule, endpoint=view_name,
                             view_func=view_func, **options)


if __name__ == '__main__':
    channel = grpc.insecure_channel('localhost:4001')
    stub = HelloStub(channel)

    msg = HelloRequest(name='lishuo zhuang')
    response = stub.hello(msg)
    print(response.greeting)

    msg = HelloRequest(name='fei wu')
    response = stub.hello(msg)
    print(response.greeting)

    register_urlpatterns(app)
    from waitress import serve
    serve(app, host=settings.host, port=settings.port)
    # app.run(host=settings.host, port=settings.port)
