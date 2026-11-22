// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00321 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const _coerced = Math.max(0, Math.min(parseInt(String(userInput), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const recordCount = boundedVal;
  if (!Number.isInteger(recordCount) || recordCount < 0 || recordCount > 16384) { res.status(400).json({ error: "too many records" }); return; }
  const table = new ArrayBuffer(recordCount * 64);
  res.json({ allocated: table.byteLength }); return;
}
