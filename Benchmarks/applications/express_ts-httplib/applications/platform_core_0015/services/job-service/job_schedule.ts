// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const scheduleJob = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const note = (await _cache.get("user_data")) || "";
  const _raw = note;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://platform-api:8080/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ accepted: true });
}
