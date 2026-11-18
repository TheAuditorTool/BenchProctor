// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const queryDashboard = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const cohort: string = parts.join(',');
  await fetch("http://retention-service:8080/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
