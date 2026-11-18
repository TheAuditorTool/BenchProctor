// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const mergeIndex = async (req: Request, res: Response): Promise<void> => {
  const subtitle = ((req as any).file?.originalname as string) || "";
  const ledger = String(subtitle).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(ledger)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = ledger;
  fs.writeFileSync("/var/uploads/" + remittance, "data");
  res.json({ accepted: true });
}
