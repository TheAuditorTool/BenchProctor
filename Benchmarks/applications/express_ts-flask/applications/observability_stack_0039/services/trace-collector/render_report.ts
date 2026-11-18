// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderReport = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const cohort: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(cohort)) { res.status(403).json({error:'forbidden'}); return; }
  const gauge = cohort;
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
