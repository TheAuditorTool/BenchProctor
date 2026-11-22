// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00335 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).files?.[0]?.originalname as string) || "";
  const data = String(userInput).slice(0, 200);
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}
