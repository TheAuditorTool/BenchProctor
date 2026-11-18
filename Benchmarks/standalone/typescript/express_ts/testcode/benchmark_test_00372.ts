// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00372 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(String(parsedNum));
  res.json({ accepted: true });
}
