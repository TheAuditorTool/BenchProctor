// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00700 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}
