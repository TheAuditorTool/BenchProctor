// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00013 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const [data] = String(userInput).split(',');
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ accepted: true });
}
