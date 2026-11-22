// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00054 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = userInput != null ? userInput : '';
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.app.locals.announcement = String(parsedNum);
  res.json({ accepted: true });
}
