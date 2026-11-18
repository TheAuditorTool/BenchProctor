// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const scoreAnomaly = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(excerpt);
  await fetch("http://alert-router:8080/route_alert", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
