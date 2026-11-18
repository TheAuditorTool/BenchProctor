// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00095 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ accepted: true });
}
