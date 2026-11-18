// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00187 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = `${userInput}`;
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ accepted: true });
}
