from flask import Flask, request, stream_with_context, Response
from concurrent.futures import ThreadPoolExecutor
import sys
import grpc
from protoc.trainer_pb2_grpc import ModelTrainerStub
from protoc.trainer_pb2 import ModelTrainerRequest
import settings
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

EXECUTOR = ThreadPoolExecutor()

@app.route('/train_model', methods=['GET', 'POST'])
def train_model():
    r = request.args
    code = r['code']

    channel = grpc.insecure_channel(f'{settings.rpc_host}:{settings.rpc_port}')
    stub = ModelTrainerStub(channel)

    rpc_msg = ModelTrainerRequest(code=code)
    log_iterator = stub.train(rpc_msg)

    def generate():
        for log in log_iterator:
            yield log.log

    # return generate(), {'Content-Type', "text/event-stream"}
        
    response = app.response_class(stream_with_context(generate()))
    # response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Content-Type', 'text/event-stream')
    # response.headers.add('Cache-Control', 'no-cache')
    # response.headers.add('Connection', 'keep-alive')
    # response.headers.add('X-Accel-Buffering', 'no')
    return response

# @app.route('/1.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')

def get_url_patterns():
    urlPrefix = '/api/v1/trainer'
    urlPatterns = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint == 'static':
            continue
        urlPatterns.append((urlPrefix + str(rule), getattr(
            sys.modules[__name__], rule.endpoint), {'methods': list(rule.methods)}))
        
    return urlPatterns
