// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00054 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  if (!/^[a-zA-Z0-9 _.%~\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  res.json({ accepted: true });
}
