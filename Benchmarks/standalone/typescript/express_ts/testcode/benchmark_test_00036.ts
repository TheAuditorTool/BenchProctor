// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00036 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.session.data = String(processed);
  res.json({ accepted: true });
}
