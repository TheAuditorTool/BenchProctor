// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00619 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  res.cookie("session", data, { httpOnly: true, sameSite: "strict" });
  res.json({ accepted: true });
}
