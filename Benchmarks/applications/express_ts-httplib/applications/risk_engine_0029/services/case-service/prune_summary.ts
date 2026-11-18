// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const pruneSummary = async (req: Request, res: Response): Promise<void> => {
  const subject = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _input = String(subject);
  let grievance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': grievance = _input.normalize('NFC'); break;
    default: grievance = _input; break;
  }
  const resolved = path.resolve("/var/app/data", grievance);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const verdict = resolved;
  fs.writeFileSync(verdict, "data");
  res.json({ accepted: true });
}
