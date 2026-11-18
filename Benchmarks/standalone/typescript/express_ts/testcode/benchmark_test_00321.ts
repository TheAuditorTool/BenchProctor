// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00321 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  eval(data);
  res.json({ accepted: true });
}
