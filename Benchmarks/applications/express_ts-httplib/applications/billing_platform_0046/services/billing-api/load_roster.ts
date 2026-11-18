// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";
import { createClient } from "redis";

export const loadRoster = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const remark = (await _cache.get("user_data")) || "";
  const _input = String(remark);
  let remittance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': remittance = _input.normalize('NFC'); break;
    default: remittance = _input; break;
  }
  http.get(remittance);
  res.json({ accepted: true });
}
