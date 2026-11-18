// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00593 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  req.session.data = String(data);
  res.json({ accepted: true });
}
