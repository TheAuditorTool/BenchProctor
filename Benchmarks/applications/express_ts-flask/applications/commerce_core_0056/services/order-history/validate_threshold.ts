// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateThreshold = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(backorder)) { res.status(403).json({error:'forbidden'}); return; }
  const voucher = backorder;
  childProcess.execSync("echo " + voucher);
  res.json({ accepted: true });
}
