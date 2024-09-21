"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.config = exports.configs = void 0;
const dev_1 = __importDefault(require("./us/dev"));
const dev_2 = __importDefault(require("./cn/dev"));
exports.configs = { us_dev: dev_1.default, cn_dev: dev_2.default };
const configName = `${process.env.REGION}_${process.env.ENV}`;
exports.config = exports.configs[configName];
