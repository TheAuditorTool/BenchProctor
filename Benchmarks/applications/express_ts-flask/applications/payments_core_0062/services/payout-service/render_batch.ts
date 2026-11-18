// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderBatch = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(headline).split(',')) { parts.push(token); }
  const disbursement: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(disbursement)) { res.status(403).json({error:'forbidden'}); return; }
  const remittance = disbursement;
  childProcess.execSync("echo " + remittance);
  res.json({ accepted: true });
}
