// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00056 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(String(parsedNum));
  res.json({ accepted: true });
}
