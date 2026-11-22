// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00119 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  JSON.parse(data);
  res.json({ accepted: true });
}
