// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00012 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  JSON.parse(data);
  res.json({ accepted: true });
}
