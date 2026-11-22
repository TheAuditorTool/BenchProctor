// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00058 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const emailMatch = String(userInput).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { res.status(400).json({ error: "not an email address" }); return; }
  const domain = emailMatch[1];
  res.json({ domain }); return;
}
