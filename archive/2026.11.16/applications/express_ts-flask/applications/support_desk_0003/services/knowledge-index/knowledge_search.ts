// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const searchKnowledge = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.host as string) || "";
  const grievance = `${citation}`;
  await fetch("http://escalation-service:8000/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
