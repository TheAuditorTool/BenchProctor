// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00237 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(userInput)) { res.status(400).json({error:"invalid"}); return; }
  const processed = userInput;
  Object.assign(req.session, { data: String(processed), expiresAt: Date.now() + 900000 });
  res.json({ accepted: true });
}
