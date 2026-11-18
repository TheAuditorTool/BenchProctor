// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const sweepRetention = async (req: Request, res: Response): Promise<void> => {
  const headline = ((req as any).file?.originalname as string) || "";
  const cohort = headline != null ? headline : '';
  await fetch("http://dashboard-api:8000/query_dashboard", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
