// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00021 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const [data] = String(userInput).split(',');
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ accepted: true });
}
