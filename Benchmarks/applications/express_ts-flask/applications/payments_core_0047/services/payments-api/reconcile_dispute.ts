// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const reconcileDispute = async (req: Request, res: Response): Promise<void> => {
  const footnote = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(footnote).split(',')) { parts.push(token); }
  const remittance: string = parts.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(remittance)) { res.status(403).json({error:"forbidden"}); return; }
  const disbursement = "/var/app/data/" + remittance;
  fs.writeFileSync(disbursement, "data");
  res.json({ accepted: true });
}
