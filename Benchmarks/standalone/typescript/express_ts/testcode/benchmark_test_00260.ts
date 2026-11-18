// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00260 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  eval(processed);
  res.json({ accepted: true });
}
