// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00097 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
  res.json({ accepted: true });
}
