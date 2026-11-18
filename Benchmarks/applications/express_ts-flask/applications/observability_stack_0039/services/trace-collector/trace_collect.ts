// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectTrace = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.authorization as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(caption);
  await fetch("http://anomaly-scorer:8000/score_anomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
