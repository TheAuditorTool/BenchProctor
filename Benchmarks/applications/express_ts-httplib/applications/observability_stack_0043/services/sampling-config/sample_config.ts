// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const configureSample = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  const gauge = note != null ? note : '';
  await fetch("http://retention-service:8080/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
