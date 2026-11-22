// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const ingestMetric = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.params.id as string) || "";
  (globalThis as any).lastRequestValue = tagline;
  const gauge: string = (globalThis as any).lastRequestValue;
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://dashboard-api:8000/query_dashboard", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
