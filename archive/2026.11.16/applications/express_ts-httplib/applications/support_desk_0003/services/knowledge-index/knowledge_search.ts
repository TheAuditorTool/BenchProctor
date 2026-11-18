// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const searchKnowledge = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const grievance: string = parts.join(',');
  await fetch("http://escalation-service:8080/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
