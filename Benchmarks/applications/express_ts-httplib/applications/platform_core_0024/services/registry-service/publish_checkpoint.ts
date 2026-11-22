// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

export const publishCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const heading = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = heading;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const persona = handshake;
  const fileContent = fs.readFileSync("/var/app/data/" + persona, "utf8");
  res.send(fileContent);
}
