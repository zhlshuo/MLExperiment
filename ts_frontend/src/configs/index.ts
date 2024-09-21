import us_dev from "./us/dev";
import cn_dev from "./cn/dev";

export const configs = { us_dev, cn_dev };
const configName = `${process.env.REGION}_${process.env.ENV}`
export const config = configs[configName as keyof typeof configs]