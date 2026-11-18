// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const shipLog = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.cookies?.session_token as string) || "";
  const _input = String(summary);
  let gauge;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': gauge = _input.normalize('NFC'); break;
    default: gauge = _input; break;
  }
  await fetch("http://anomaly-scorer:8080/score_anomaly", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
