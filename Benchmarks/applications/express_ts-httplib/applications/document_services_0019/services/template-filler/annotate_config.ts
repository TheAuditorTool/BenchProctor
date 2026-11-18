// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const annotateConfig = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const dossier: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(dossier))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  await db.query("SELECT * FROM users ORDER BY " + addendum);
  res.json({ accepted: true });
}
