// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00631 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ accepted: true });
}
