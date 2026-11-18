// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00618 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}
