// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const reconcileThreshold = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _input = String(synopsis);
  let verdict;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': verdict = _input.normalize('NFC'); break;
    default: verdict = _input; break;
  }
  const resolved = path.resolve("/var/app/data", verdict);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = resolved;
  fs.writeFileSync(grievance, "data");
  res.json({ accepted: true });
}
