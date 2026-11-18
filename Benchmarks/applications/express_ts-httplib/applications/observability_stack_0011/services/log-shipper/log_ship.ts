// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const shipLog = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers["x-custom-header"] as string) || "";
  const gauge = caption != null ? caption : '';
  await fetch("http://metrics-ingest:8080/ingest_metric", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
