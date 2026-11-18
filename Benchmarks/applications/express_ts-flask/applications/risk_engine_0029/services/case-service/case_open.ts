// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openCase = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers.authorization as string) || "";
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(subject);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://screening-service:8000/run_screening", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: grievance})});
  res.json({ accepted: true });
}
