// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const pruneRendition = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(notice).split(',')) { parts.push(token); }
  const rendition: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(rendition))) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  await db.query("SELECT * FROM users ORDER BY " + montage);
  res.json({ accepted: true });
}
