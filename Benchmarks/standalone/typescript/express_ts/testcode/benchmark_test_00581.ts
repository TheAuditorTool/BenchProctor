// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00581 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const [data] = String(userInput).split(',');
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
