// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as libxmljs from "libxmljs";
import * as nodeUtil from "util";

export const BenchmarkTest00226 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = nodeUtil.format("%s", userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true } as libxmljs.XMLParseOptions);
  res.json({ accepted: true });
}
