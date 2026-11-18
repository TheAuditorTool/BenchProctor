// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as zod from "zod";

export const BenchmarkTest00058 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).slice(0, 200);
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  req.session.data = String(processed);
  res.json({ accepted: true });
}
