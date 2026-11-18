// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00309 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(userInput));
  res.json({ accepted: true });
}
