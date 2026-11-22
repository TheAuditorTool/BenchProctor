// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectTrace = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(paragraph).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  await fetch("http://sampling-config:8000/configure_sample", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
