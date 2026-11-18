// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";
import * as nodeUtil from "util";

export const BenchmarkTest00045 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}
