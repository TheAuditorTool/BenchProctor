// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00284 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = Buffer.from(userInput, "hex").toString();
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
