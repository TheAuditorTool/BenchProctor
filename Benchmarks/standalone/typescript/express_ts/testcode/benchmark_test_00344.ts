// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00344 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}
