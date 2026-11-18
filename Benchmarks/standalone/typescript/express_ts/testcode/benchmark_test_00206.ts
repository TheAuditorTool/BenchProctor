// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00206 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(String(parsedNum));
  res.json({ accepted: true });
}
