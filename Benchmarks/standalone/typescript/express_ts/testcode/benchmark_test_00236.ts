// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";
import * as nodeUtil from "util";

export const BenchmarkTest00236 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const data = nodeUtil.format("%s", userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
