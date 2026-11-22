// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00168 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { res.status(400).json({ error: "not an email address" }); return; }
  const domain = emailMatch[1];
  res.json({ domain }); return;
}
