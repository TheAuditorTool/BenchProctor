// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00318 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const data = String(userInput).slice(0, 200);
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}
