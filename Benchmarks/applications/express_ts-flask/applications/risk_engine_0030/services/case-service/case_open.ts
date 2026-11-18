// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openCase = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.field as string) || "";
  const payload = { get value() { return summary; } };
  const grievance = payload.value;
  await fetch("http://alert-triage:8000/triage_alert", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: grievance})});
  res.json({ accepted: true });
}
