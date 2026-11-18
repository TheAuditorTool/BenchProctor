// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00651 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const data = String(userInput).slice(0, 200);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
