// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const ingestMetric = async (req: Request, res: Response): Promise<void> => {
  const note = (await shared.mq.receive("app-events"));
  const formData = Object.freeze({ payload: note });
  const cohort = formData.payload;
  await fetch("http://log-shipper:8080/ship_log", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
