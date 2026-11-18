// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00460 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  eval(data);
  res.json({ accepted: true });
}
