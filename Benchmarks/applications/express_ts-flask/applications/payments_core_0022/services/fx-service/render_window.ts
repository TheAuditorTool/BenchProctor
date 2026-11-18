// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderWindow = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(subject).split(',')) { parts.push(token); }
  const ledger: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(ledger)) { res.status(403).json({error:'forbidden'}); return; }
  const disbursement = ledger;
  childProcess.execSync("echo " + disbursement);
  res.json({ accepted: true });
}
