// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00134 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  new Function("return (" + String(parsedNum) + ");")();
  res.json({ accepted: true });
}
