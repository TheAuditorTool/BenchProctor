// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00042 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  new Function("return (" + String(data) + ");")();
  res.json({ accepted: true });
}
