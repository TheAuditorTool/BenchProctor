// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const buildBatch = async (req: Request, res: Response): Promise<void> => {
  const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = tagline;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const note = persona;
  const fileContent = fs.readFileSync("/var/app/data/" + note, "utf8");
  res.send(fileContent);
}
