// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const compactPolicy = async (req: Request, res: Response): Promise<void> => {
  const wording = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(wording).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(handshake)) { res.status(403).json({error:"forbidden"}); return; }
  const subject = "/var/app/data/" + handshake;
  fs.writeFileSync(subject, "data");
  res.json({ accepted: true });
}
