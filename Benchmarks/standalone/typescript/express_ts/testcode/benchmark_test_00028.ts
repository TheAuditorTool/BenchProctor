// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00028 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { res.status(400).json({ error: "out of range" }); return; }
  const buf = Buffer.alloc(requested + 1);
  res.json({ allocated: buf.length }); return;
}
