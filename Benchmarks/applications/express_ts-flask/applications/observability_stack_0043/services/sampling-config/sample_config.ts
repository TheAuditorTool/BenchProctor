// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const configureSample = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers["user-agent"] as string) || "";
  const gauge = nodeUtil.format("%s", note);
  await fetch("http://retention-service:8000/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
