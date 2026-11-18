// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00575 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
