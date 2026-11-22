// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00024 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const [data] = String(userInput).split(',');
  parseXmlString(String(data), { noent: true, dtdload: true, nonet: false });
  res.json({ accepted: true });
}
