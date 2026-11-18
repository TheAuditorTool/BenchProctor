// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00289 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = `${userInput}`;
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}
