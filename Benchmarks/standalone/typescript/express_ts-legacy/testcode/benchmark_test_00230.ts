// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00230 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = decodeURIComponent(userInput);
  const _desKey = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY ?? (() => { throw new Error("DATA_ENC_KEY is not set"); })()).digest().subarray(0, 24);
  crypto.createCipheriv("des-ede3-ecb", _desKey, null).update(String(data));
  res.json({ accepted: true });
}
