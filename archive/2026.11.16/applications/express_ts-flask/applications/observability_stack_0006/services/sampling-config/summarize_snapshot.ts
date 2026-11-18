// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const summarizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const preface = ((req as any).file?.originalname as string) || "";
  const cohort = String(preface).slice(0, 200);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(cohort)) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  fs.writeFileSync("/var/uploads/" + gauge, "data");
  res.json({ accepted: true });
}
