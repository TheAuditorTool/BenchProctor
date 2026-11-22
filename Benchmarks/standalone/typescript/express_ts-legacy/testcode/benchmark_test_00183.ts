// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00183 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  Object.assign(req.session, { data: String(data), expiresAt: Date.now() + 900000 });
  res.json({ accepted: true });
}
