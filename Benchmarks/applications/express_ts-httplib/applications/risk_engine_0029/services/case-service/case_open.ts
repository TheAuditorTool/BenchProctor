// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const openCase = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers["user-agent"] as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(subject);
  const grievance: string = readInput();
  await fetch("http://screening-service:8080/run_screening", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: grievance})});
  res.json({ accepted: true });
}
