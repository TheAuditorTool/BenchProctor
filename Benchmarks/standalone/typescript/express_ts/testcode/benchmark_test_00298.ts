// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00298 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
  const boundedVal = _coerced;
  const quantity = boundedVal;
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > 1000) { res.status(400).json({ error: "quantity out of range" }); return; }
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}
