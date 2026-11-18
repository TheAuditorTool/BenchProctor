// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const summarizeThreshold = async (req: Request, res: Response): Promise<void> => {
  const snippet = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _input = String(snippet);
  let handshake;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': handshake = _input.normalize('NFC'); break;
    default: handshake = _input; break;
  }
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const paragraph = resolved;
  fs.writeFileSync(paragraph, "data");
  res.json({ accepted: true });
}
