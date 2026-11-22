// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const checkSla = async (req: Request, res: Response): Promise<void> => {
  const preface = process.env.SUPPORT_INPUT_0036 || "";
  const pending: string[] = String(preface).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const grievance: string = collected.join(',');
  await fetch("http://escalation-service:8080/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
