// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const scoreAnomaly = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const gauge: string = transform(excerpt);
  await fetch("http://alert-router:8000/route_alert", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
