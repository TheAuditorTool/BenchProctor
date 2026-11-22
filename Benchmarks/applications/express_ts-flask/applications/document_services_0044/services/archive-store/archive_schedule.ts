// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const archiveSchedule = async (req: Request, res: Response): Promise<void> => {
  const phrase = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(phrase).split(',')) { parts.push(token); }
  const dossier: string = parts.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(dossier)) { res.status(403).json({error:"forbidden"}); return; }
  const addendum = "/var/app/data/" + dossier;
  fs.writeFileSync(addendum, "data");
  res.json({ accepted: true });
}
