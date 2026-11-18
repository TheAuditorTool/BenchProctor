// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";
import * as zod from "zod";

export const BenchmarkTest00192 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%~\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + processed + "']", xmlDoc);
  res.json({ accepted: true });
}
