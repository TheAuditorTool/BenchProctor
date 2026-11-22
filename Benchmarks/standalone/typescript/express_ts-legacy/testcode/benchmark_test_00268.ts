// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const BenchmarkTest00268 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-forwarded-for"] as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const quantity = boundedVal;
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > 1000) { res.status(400).json({ error: "quantity out of range" }); return; }
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}
