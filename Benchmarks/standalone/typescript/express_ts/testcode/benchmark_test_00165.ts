// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00165 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { res.status(400).json({ error: "not an email address" }); return; }
  const domain = emailMatch[1];
  res.json({ domain }); return;
}
