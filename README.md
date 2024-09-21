# MultiProjectTemplate
# first time running, create venv
python -m venv env

# lanuch python rpc server in new terminal
source ./env/bin/activate
SERVER=python_rpc_server make run

# lanuch python rest server in new terminal
source ./env/bin/activate
SERVER=python_rest_server make run

# lanuch java server in new terminal
SERVER=java_websocket_server_maven make run

# lanuch react_frontend server - react in new terminal
nvm use 20.10.0
SERVER=react_frontend REGION=us ENV=dev make run

# lanuch ts_frontend server - express
# SERVER=ts_frontend make run