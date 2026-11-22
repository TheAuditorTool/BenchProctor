// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const enrichRecord = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-forwarded-for"] as string) || "";
  const remittance = footnote != null ? footnote : '';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const arrears = remittance;
  fs.writeFileSync("/var/uploads/" + arrears, "data");
  res.json({ accepted: true });
}
