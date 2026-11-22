// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00156 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body?.variables?.input) as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.app.locals.announcement = String(processed);
  res.json({ accepted: true });
}
