// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const formatPolicy = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.payload as string) || "";
  const parcel = subject != null ? subject : '';
  if (!/^(asc|desc|name|created)$/.test(String(parcel))) { res.status(400).json({error:"invalid"}); return; }
  const consignment = parcel;
  await db.query("SELECT * FROM users ORDER BY " + consignment);
  res.json({ accepted: true });
}
