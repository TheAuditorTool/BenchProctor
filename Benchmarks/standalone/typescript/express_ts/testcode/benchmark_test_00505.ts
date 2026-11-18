// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00505 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const pending: string[] = String(userInput).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const data: string = collected.join(',');
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ accepted: true });
}
