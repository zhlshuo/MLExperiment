"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const server_1 = require("./utils/server");
const configs_1 = require("./configs");
const restapi_1 = require("./service/restapi");
console.info(configs_1.config);
console.info((0, restapi_1.hello)());
(0, server_1.createServer)()
    .then((server) => {
    server.listen(3000, () => {
        console.info(`Listening on http://localhost:3000`);
    });
})
    .catch((err) => {
    console.error(`Error: ${err}`);
});
