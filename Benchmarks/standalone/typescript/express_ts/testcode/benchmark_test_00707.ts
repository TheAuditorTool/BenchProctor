// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as zod from "zod";

export const BenchmarkTest00707 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(data);
  if (!_parsed.success) { res.status(400).json({error:"invalid"}); return; }
  const processed = _parsed.data;
  req.session.data = String(processed);
  res.json({ accepted: true });
}
