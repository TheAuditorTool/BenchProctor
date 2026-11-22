// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00326 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.app.locals.announcement = String(processed);
  res.json({ accepted: true });
}
