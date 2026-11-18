// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const enrichHeader = async (req: Request, res: Response): Promise<void> => {
  const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const bulletin = String(summary).slice(0, 200);
  const resolved = path.resolve("/var/app/data", bulletin);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const snippet = resolved;
  fs.writeFileSync(snippet, "data");
  res.json({ accepted: true });
}
