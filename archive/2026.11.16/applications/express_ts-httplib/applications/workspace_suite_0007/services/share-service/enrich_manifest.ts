// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const enrichManifest = async (req: Request, res: Response): Promise<void> => {
  const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const payload = { get value() { return summary; } };
  const subtitle = payload.value;
  if (!/^(asc|desc|name|created)$/.test(String(subtitle))) { res.status(400).json({error:"invalid"}); return; }
  const notice = subtitle;
  const fileContent = fs.readFileSync("/var/app/data/" + notice, "utf8");
  res.send(fileContent);
}
