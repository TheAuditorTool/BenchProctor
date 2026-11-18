// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const pruneSnapshot = async (req: Request, res: Response): Promise<void> => {
  const note = (req.query.id as string) || "";
  const [inquiry] = String(note).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(inquiry)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = inquiry;
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
