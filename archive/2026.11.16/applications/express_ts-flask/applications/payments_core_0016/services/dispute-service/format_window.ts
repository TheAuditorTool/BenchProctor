// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatWindow = async (req: Request, res: Response): Promise<void> => {
  const passage = ((req as any).file?.originalname as string) || "";
  const remittance = String(passage).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const disbursement = remittance;
  fs.writeFileSync("/var/uploads/" + disbursement, "data");
  res.json({ accepted: true });
}
