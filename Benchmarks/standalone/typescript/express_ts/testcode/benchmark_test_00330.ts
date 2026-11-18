// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00330 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
