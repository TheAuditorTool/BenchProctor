// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00069 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const recordCount = parseInt(String(userInput), 10);
  const table = new ArrayBuffer((recordCount * 64) >>> 0);
  res.json({ allocated: table.byteLength }); return;
}
