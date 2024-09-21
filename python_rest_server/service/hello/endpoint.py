from flask import Flask, request, jsonify
from common.mysql import testSession
from models.hello import Hello
import sys
import grpc
from protoc.hello_pb2_grpc import HelloStub
from protoc.hello_pb2 import HelloRequest
from protoc.loader_pb2_grpc import ImageLoaderStub
from protoc.loader_pb2 import ImageLoaderRequest
from protoc.trainer_pb2_grpc import ModelTrainerStub
from protoc.trainer_pb2 import ModelTrainerRequest
from protoc.streaming_pb2_grpc import StreamingStub
from protoc.streaming_pb2 import StreamingRequest
import settings
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    r = request.args
    name = r['name']
    hello = testSession.query(Hello).filter(Hello.name.contains(name)).first()
    response = jsonify(data=str(hello))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/rpc', methods=['GET', 'POST'])
def hello_rpc():
    r = request.args
    name = r['name']

    channel = grpc.insecure_channel(f'{settings.rpc_host}:{settings.rpc_port}')
    stub = HelloStub(channel)

    rpc_msg = HelloRequest(name=name)
    rpc_response = stub.hello(rpc_msg)
    response = jsonify(data=str(rpc_response.greeting))
    print(rpc_response.greeting)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/load_image', methods=['GET', 'POST'])
def load_image():
    r = request.args
    name = r['name']

    channel = grpc.insecure_channel(f'{settings.rpc_host}:{settings.rpc_port}')
    stub = ImageLoaderStub(channel)

    rpc_msg = ImageLoaderRequest(name=name)
    rpc_response = stub.load(rpc_msg)
    response = jsonify(data=str(rpc_response.isFinished))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/train_model', methods=['GET', 'POST'])
def train_model():
    channel = grpc.insecure_channel(f'{settings.rpc_host}:{settings.rpc_port}')
    stub = ModelTrainerStub(channel)

    rpc_msg = ModelTrainerRequest()
    rpc_response = stub.train(rpc_msg)
    response = jsonify(data=str(rpc_response.isFinished))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/streaming_call', methods=['GET', 'POST'])
def streaming_call():
    channel = grpc.insecure_channel(f'{settings.rpc_host}:{settings.rpc_port}')
    stub = StreamingStub(channel)

    r = request.args
    code = r['code']

    rpc_msg = StreamingRequest(code=code)
    rpc_response_iterator = stub.call(rpc_msg)
    for res in rpc_response_iterator:
        print(f'streaming_call: {res}')
    response = jsonify(data='done')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# @app.route('/1.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')

def get_url_patterns():
    urlPrefix = '/api/v1/hello'
    urlPatterns = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint == 'static':
            continue
        urlPatterns.append((urlPrefix + str(rule), getattr(
            sys.modules[__name__], rule.endpoint), {'methods': list(rule.methods)}))
        
    return urlPatterns
