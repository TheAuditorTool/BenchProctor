// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const normalizeReport = async (req: Request, res: Response): Promise<void> => {
  const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _input = String(transcript);
  let rendition;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': rendition = _input.normalize('NFC'); break;
    default: rendition = _input; break;
  }
  const resolved = path.resolve("/var/app/data", rendition);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const montage = resolved;
  fs.writeFileSync(montage, "data");
  res.json({ accepted: true });
}
