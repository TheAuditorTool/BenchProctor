// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectTrace = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.origin as string) || "";
  const _input = String(paragraph);
  let gauge;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': gauge = _input.normalize('NFC'); break;
    default: gauge = _input; break;
  }
  await fetch("http://sampling-config:8080/configure_sample", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
