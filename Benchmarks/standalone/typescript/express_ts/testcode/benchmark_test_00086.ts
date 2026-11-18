// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00086 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
