// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00472 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ accepted: true });
}
