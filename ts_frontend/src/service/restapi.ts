import axios from "axios";

import { config } from "../configs";

export const hello = async () => {
  const response = await axios.get(config["restApiBaseUrl"] + "api/v1/hello?name=fei");
  return response;
};
