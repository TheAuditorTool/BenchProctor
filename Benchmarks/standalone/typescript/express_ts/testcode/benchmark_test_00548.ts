// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00548 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ accepted: true });
}
