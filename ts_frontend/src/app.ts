// import { Alert } from "react-native";
import { createServer } from "./utils/server";
// import { config } from "./configs";
import { hello } from "./service/restapi";

hello().then((res) => {
  // Alert.alert(JSON.stringify(res));
  console.info(res.data);
});

createServer()
  .then((server) => {
    server.listen(3000, () => {
      console.info(`Listening on http://localhost:3000`);
    });
  })
  .catch((err) => {
    console.error(`Error: ${err}`);
  });
