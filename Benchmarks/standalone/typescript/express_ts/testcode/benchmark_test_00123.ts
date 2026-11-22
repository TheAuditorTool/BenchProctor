// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00123 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.payload as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const minstd = { state: (Date.now() % 2147483646) + 1, next() { this.state = (this.state * 48271) % 2147483647; return this.state; } };
  const token = minstd.next().toString(36) + minstd.next().toString(36) + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}
