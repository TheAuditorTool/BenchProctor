// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";
import * as nodeUtil from "util";

export const BenchmarkTest00208 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const data = nodeUtil.format("%s", userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ accepted: true });
}
