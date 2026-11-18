// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const BenchmarkTest00558 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await shared.mq.receive("app-events"));
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  await db.query("SELECT * FROM users ORDER BY " + processed);
  res.json({ accepted: true });
}
