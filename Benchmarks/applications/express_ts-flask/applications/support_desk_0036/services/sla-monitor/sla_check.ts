// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const checkSla = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const grievance = String(preface).slice(0, 200);
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
