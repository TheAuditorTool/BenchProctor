// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00327 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.parse("//user[name='" + parsedNum + "']").select({ node: usersDoc });
  res.json({ accepted: true });
}
