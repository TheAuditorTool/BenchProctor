// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const publishMessage = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const summary = (await _cache.get("user_data")) || "";
  const _input = String(summary);
  let bulletin;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': bulletin = _input.normalize('NFC'); break;
    default: bulletin = _input; break;
  }
  await fetch("http://bounce-handler:8080/record_bounce", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ accepted: true });
}
