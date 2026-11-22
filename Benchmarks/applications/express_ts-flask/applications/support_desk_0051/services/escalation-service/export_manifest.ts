// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const exportManifest = async (req: Request, res: Response): Promise<void> => {
  const preface = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const grievance: string = parts.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(grievance)) { res.status(403).json({error:"forbidden"}); return; }
  const inquiry = "/var/app/data/" + grievance;
  fs.writeFileSync(inquiry, "data");
  res.json({ accepted: true });
}
