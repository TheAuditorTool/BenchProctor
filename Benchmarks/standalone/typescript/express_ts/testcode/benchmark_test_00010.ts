// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00010 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  req.session.data = String(data);
  res.json({ accepted: true });
}
