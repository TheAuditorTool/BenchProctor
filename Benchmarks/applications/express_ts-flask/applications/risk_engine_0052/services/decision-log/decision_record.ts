// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const recordDecision = async (req: Request, res: Response): Promise<void> => {
  const memo = ((req as any).files?.[0]?.originalname as string) || "";
  const parts: string[] = [];
  for (const token of String(memo).split(',')) { parts.push(token); }
  const verdict: string = parts.join(',');
  await fetch("http://screening-service:8000/run_screening", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ accepted: true });
}
