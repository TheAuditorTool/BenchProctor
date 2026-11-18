// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadSummary = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(gauge)) { res.status(403).json({error:'forbidden'}); return; }
  const cohort = gauge;
  childProcess.execSync("echo " + cohort);
  res.json({ accepted: true });
}
