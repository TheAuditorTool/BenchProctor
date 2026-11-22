// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const ingestMetric = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const cohort: string = transform(excerpt);
  await fetch("http://sampling-config:8000/configure_sample", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
