// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";
import { createClient } from "redis";

export const reconcileRecord = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const synopsis = (await _cache.get("user_data")) || "";
  const _input = String(synopsis);
  let byline;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': byline = _input.normalize('NFC'); break;
    default: byline = _input; break;
  }
  http.get(byline);
  res.json({ accepted: true });
}
