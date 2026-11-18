// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneReport = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).file?.originalname as string) || "";
  const bulletin = String(summary).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const notice = bulletin;
  fs.writeFileSync("/var/uploads/" + notice, "data");
  res.json({ accepted: true });
}
