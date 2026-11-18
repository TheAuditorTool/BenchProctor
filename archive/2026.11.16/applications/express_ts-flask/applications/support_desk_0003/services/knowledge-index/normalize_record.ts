// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const normalizeRecord = async (req: Request, res: Response): Promise<void> => {
  const citation = ((req as any).file?.originalname as string) || "";
  const grievance = String(citation).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(grievance)) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  fs.writeFileSync("/var/uploads/" + inquiry, "data");
  res.json({ accepted: true });
}
