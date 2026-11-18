// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const queryDashboard = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(summary);
  await fetch("http://retention-service:8000/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
