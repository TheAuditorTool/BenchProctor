// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00043 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const [data] = String(userInput).split(',');
  const recordCount = parseInt(String(data), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}
