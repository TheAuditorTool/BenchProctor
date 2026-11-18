// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00439 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  req.session.data = String(parsedNum);
  res.json({ accepted: true });
}
