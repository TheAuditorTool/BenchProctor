// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const auditLedger = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const voucher: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(voucher))) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  await db.query("SELECT * FROM users ORDER BY " + backorder);
  res.json({ accepted: true });
}
