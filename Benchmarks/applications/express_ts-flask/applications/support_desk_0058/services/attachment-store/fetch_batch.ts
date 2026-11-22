// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const fetchBatch = async (req: Request, res: Response): Promise<void> => {
  const snippet = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const inquiry: string = parts.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(inquiry)) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = "/var/app/data/" + inquiry;
  fs.writeFileSync(grievance, "data");
  res.json({ accepted: true });
}
