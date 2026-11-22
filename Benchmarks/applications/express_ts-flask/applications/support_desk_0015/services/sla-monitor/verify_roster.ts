// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const verifyRoster = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  const grievance = decodeURIComponent(phrase);
  if (!/^(asc|desc|name|created)$/.test(String(grievance))) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  childProcess.execSync("echo " + inquiry);
  res.json({ accepted: true });
}
