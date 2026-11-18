// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00560 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = `${userInput}`;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.session.data = String(processed);
  res.json({ accepted: true });
}
