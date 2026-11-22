// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const ingestMetric = async (req: Request, res: Response): Promise<void> => {
  const note = (req.params.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const cohort: string = readInput();
  await fetch("http://log-shipper:8000/ship_log", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
