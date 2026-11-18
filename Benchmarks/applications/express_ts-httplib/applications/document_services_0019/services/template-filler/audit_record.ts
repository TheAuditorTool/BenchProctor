// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";
import { createClient } from "redis";

export const auditRecord = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const passage = (await _cache.get("user_data")) || "";
  const _input = String(passage);
  let dossier;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': dossier = _input.normalize('NFC'); break;
    default: dossier = _input; break;
  }
  http.get(dossier);
  res.json({ accepted: true });
}
