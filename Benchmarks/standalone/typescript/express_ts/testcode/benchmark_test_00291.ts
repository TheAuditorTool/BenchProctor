// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00291 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body?.variables?.input) as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  new Function("return (" + String(processed) + ");")();
  res.json({ accepted: true });
}
