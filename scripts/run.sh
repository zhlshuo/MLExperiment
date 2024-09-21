#!/bin/bash
source ~/.nvm/nvm.sh
nvm use 20.10.0

server=$1
workdir=`pwd`
java_home=/home/zhlshuo/.jdks/openjdk-21.0.1/bin
react_app_region=us
react_app_env=dev

git pull

protoc_path=$workdir/protoc
rm $protoc_path/*
mkdir -p $protoc_path

idl_path=$workdir/idls
cp $idl_path/*.proto $protoc_path

export PYTHONPATH=$workdir:$PYTHONPATH
echo $PYTHONPATH

if  [[ $server == python* ]] ;
then
    python3.12 -m grpc_tools.protoc -I $workdir --python_out=$workdir --pyi_out=$workdir --grpc_python_out=$workdir $protoc_path/*.proto
    python3.12 $workdir/$server/main.py
fi

if  [[ $server == java_websocket_server_maven ]] ;
then
    $java_home/java -jar $workdir/$server/out/artifacts/java_websocket_server_maven_jar/$server.jar
fi

if  [[ $server == react_frontend ]] ;
then
    cd react_frontend
    export REACT_APP_REGION=$react_app_region
    export REACT_APP_ENV=$react_app_env
    yarn start
fi

if  [[ $server == ts_frontend ]] ;
then
    cd ts_frontend
    yarn dev
fi