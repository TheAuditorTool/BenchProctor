// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00062 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).files?.[0]?.originalname as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)![1];
  res.json({ domain }); return;
}
