// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00461 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ accepted: true });
}
