// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00004 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  const requested = parseInt(data, 10);
  const wrapped = (requested + 1) | 0;
  const buf = Buffer.alloc(wrapped);
  res.json({ allocated: buf.length }); return;
}
