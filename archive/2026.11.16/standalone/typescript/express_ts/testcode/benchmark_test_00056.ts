// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00056 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const requested = boundedVal;
  if (!Number.isFinite(requested) || requested < 0 || requested > 1048576) { res.status(400).json({ error: "out of range" }); return; }
  const buf = Buffer.alloc(requested + 1);
  res.json({ allocated: buf.length }); return;
}
