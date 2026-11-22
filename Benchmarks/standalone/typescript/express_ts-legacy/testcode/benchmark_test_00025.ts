// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00025 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}
