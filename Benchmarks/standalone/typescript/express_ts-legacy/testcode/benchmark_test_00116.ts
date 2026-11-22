// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as libxmljs from "libxmljs";

export const BenchmarkTest00116 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  res.json({ accepted: true });
}
