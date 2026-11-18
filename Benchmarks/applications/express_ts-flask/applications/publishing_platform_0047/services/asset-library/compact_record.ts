// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

export const compactRecord = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const byline = String(synopsis).slice(0, 200);
  const resolved = path.resolve("/var/app/data", byline);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const addendum = resolved;
  fs.writeFileSync(addendum, "data");
  res.json({ accepted: true });
}
