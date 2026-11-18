// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const applyMacro = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-custom-header"] as string) || "";
  const _raw = summary;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
