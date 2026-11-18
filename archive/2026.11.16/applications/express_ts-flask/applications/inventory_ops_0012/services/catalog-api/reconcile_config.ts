// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileConfig = async (req: Request, res: Response): Promise<void> => {
  const phrase = ((req as any).file?.originalname as string) || "";
  const backorder = String(phrase).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  fs.writeFileSync("/var/uploads/" + restock, "data");
  res.json({ accepted: true });
}
