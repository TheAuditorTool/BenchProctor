// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00204 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}
