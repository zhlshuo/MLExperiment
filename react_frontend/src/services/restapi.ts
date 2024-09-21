import axios from "axios";

import { config } from "../configs";

export const hello = async () => {
  const response = await axios.get(config["restApiBaseUrl"] + "api/v1/hello/?name=fei");
  return response;
};

export const hello_rpc = async () => {
  const param = "lishuo zhuang"
  const response = await axios.get(config["restApiBaseUrl"] + `api/v1/hello/rpc?name=${param}`);
  return response;
};

export const load_image = async () => {
  const param = "./datasets/cifar-10-python/cifar-10-batches-py"
  // const param = "./datasets/cifar-10-python.tar.gz"
  const response = await axios.get(config["restApiBaseUrl"] + `api/v1/hello/load_image?name=${param}`);
  return response;
};

export const train_model = async (code:any) => {
  const response = await axios.get(config["restApiBaseUrl"] + `api/v1/trainer/train_model?code=${code}`);
  return response;
};

export const streaming_call = async (code:any) => {
  const response = await axios.get(config["restApiBaseUrl"] + `api/v1/hello/streaming_call?code=${code}`);
  return response;
};