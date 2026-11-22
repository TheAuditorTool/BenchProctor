// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const fetchRecord = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-forwarded-for"] as string) || "";
  const remittance = footnote != null ? footnote : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  fs.writeFileSync("/var/uploads/" + disbursement, "data");
  res.json({ accepted: true });
}
