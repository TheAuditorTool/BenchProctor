// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { parseXmlString } from "libxmljs2";

export const BenchmarkTest00116 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = String(userInput).replace(/\u0000/g, "");
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ accepted: true });
}
