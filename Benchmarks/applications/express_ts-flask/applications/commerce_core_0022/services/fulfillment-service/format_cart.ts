// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const formatCart = async (req: Request, res: Response): Promise<void> => {
  const subject = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(subject).split(',')) { parts.push(token); }
  const voucher: string = parts.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(voucher)) { res.status(403).json({error:"forbidden"}); return; }
  const backorder = "/var/app/data/" + voucher;
  fs.writeFileSync(backorder, "data");
  res.json({ accepted: true });
}
