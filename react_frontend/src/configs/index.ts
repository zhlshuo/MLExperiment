import us_dev from "./us/dev";
import cn_dev from "./cn/dev";

const { REACT_APP_REGION, REACT_APP_ENV } = process.env;
const configName = `${REACT_APP_REGION}_${REACT_APP_ENV}`
export const configs = { us_dev, cn_dev };
export const config = configs[configName as keyof typeof configs]