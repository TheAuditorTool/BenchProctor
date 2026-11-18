// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolveDigest = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const [grievance] = String(summary).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(grievance)) { res.status(400).json({error:"invalid"}); return; }
  const verdict = grievance;
  childProcess.execSync("echo " + verdict);
  res.json({ accepted: true });
}
