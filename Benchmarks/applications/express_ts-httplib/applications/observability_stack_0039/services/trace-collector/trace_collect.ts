// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectTrace = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body as string) || "";
  const parts: string[] = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const cohort: string = parts.join(',');
  await fetch("http://anomaly-scorer:8080/score_anomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
