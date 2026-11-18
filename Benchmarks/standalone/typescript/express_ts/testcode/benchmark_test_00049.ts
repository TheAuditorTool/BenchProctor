// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as zod from "zod";

export const BenchmarkTest00049 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  req.session.data = String(processed);
  res.json({ accepted: true });
}
