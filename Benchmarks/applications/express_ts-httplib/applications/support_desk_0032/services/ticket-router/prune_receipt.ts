// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const pruneReceipt = async (req: Request, res: Response): Promise<void> => {
  const note = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _input = String(note);
  let inquiry;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': inquiry = _input.normalize('NFC'); break;
    default: inquiry = _input; break;
  }
  const resolved = path.resolve("/var/app/data", inquiry);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = resolved;
  fs.writeFileSync(grievance, "data");
  res.json({ accepted: true });
}
