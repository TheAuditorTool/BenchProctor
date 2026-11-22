// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const mergeLedger = async (req: Request, res: Response): Promise<void> => {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = caption;
  const synopsis = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(synopsis))) { res.status(400).json({error:"invalid"}); return; }
  const snippet = synopsis;
  const fileContent = fs.readFileSync("/var/app/data/" + snippet, "utf8");
  res.send(fileContent);
}
