// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const publishSignature = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body.payload as string) || "";
  const dossier = excerpt != null ? excerpt : '';
  if (!/^(asc|desc|name|created)$/.test(String(dossier))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  await db.query("SELECT * FROM users ORDER BY " + addendum);
  res.json({ accepted: true });
}
