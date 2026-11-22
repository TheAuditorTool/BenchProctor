// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00078 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ accepted: true });
}
