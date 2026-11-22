// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";
import * as nodeUtil from "util";

export const BenchmarkTest00171 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.multipart_field as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}
