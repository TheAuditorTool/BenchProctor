// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const formatManifest = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.payload as string) || "";
  const backorder = phrase != null ? phrase : '';
  if (!/^(asc|desc|name|created)$/.test(String(backorder))) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  await db.query("SELECT * FROM users ORDER BY " + restock);
  res.json({ accepted: true });
}
