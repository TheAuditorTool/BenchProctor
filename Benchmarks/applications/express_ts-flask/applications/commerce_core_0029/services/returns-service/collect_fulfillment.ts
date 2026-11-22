// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const collectFulfillment = async (req: Request, res: Response): Promise<void> => {
  const notice = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(notice).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
  if (!allowedFiles.has(backorder)) { res.status(403).json({error:"forbidden"}); return; }
  const voucher = "/var/app/data/" + backorder;
  fs.writeFileSync(voucher, "data");
  res.json({ accepted: true });
}
