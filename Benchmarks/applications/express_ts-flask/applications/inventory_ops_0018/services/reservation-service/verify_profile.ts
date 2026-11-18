// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const verifyProfile = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(backorder)) { res.status(403).json({error:'forbidden'}); return; }
  const restock = backorder;
  childProcess.execSync("echo " + restock);
  res.json({ accepted: true });
}
