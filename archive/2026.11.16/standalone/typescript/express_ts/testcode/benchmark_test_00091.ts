// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const BenchmarkTest00091 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  res.json({ accepted: true });
}
