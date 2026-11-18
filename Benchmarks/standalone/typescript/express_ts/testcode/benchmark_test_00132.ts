// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const BenchmarkTest00132 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(String(parsedNum));
  res.json({ accepted: true });
}
