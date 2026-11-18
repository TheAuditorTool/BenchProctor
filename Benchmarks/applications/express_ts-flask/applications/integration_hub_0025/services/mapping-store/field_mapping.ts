// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const mapField = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const footnote = (await _cache.get("user_data")) || "";
  const handshake = footnote != null ? footnote : '';
  await fetch("http://connector-api:8000/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ accepted: true });
}
