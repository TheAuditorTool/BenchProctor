// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const summarizeLedger = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers["x-forwarded-for"] as string) || "";
  const backorder = wording != null ? wording : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const voucher = backorder;
  fs.writeFileSync("/var/uploads/" + voucher, "data");
  res.json({ accepted: true });
}
