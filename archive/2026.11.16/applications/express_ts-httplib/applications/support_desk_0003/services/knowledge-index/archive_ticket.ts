// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const archiveTicket = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.payload as string) || "";
  const grievance = citation != null ? citation : '';
  if (!/^(asc|desc|name|created)$/.test(String(grievance))) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  await db.query("SELECT * FROM users ORDER BY " + inquiry);
  res.json({ accepted: true });
}
