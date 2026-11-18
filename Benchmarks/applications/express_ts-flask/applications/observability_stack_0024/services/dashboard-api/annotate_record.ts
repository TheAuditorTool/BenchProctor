// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateRecord = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const [cohort] = String(summary).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(cohort)) { res.status(400).json({error:"invalid"}); return; }
  const gauge = cohort;
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
