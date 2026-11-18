// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00641 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}
