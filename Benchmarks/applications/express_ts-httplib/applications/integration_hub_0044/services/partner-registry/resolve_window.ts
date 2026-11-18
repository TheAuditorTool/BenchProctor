// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const resolveWindow = async (req: Request, res: Response): Promise<void> => {
  const blurb = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(blurb).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const citation = handshake;
  await db.query("SELECT * FROM users ORDER BY " + citation);
  res.json({ accepted: true });
}
