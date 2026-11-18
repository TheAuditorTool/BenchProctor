// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const loadReport = async (req: Request, res: Response): Promise<void> => {
  const passage = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _input = String(passage);
  let montage;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': montage = _input.normalize('NFC'); break;
    default: montage = _input; break;
  }
  const resolved = path.resolve("/var/app/data", montage);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const rendition = resolved;
  fs.writeFileSync(rendition, "data");
  res.json({ accepted: true });
}
