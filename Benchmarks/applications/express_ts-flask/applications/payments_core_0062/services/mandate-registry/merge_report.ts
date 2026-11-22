// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const mergeReport = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers["x-forwarded-for"] as string) || "";
  const disbursement = headline != null ? headline : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(disbursement)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = disbursement;
  fs.writeFileSync("/var/uploads/" + remittance, "data");
  res.json({ accepted: true });
}
