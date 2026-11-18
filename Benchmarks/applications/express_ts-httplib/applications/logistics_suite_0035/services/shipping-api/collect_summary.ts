// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";
import { createClient } from "redis";

export const collectSummary = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const phrase = (await _cache.get("user_data")) || "";
  const _input = String(phrase);
  let parcel;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': parcel = _input.normalize('NFC'); break;
    default: parcel = _input; break;
  }
  http.get(parcel);
  res.json({ accepted: true });
}
