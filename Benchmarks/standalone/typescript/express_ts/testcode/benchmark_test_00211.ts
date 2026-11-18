// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00211 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}
