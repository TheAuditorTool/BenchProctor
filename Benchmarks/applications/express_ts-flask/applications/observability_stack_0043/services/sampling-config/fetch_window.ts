// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchWindow = async (req: Request, res: Response): Promise<void> => {
  const note = (req.query.id as string) || "";
  const [gauge] = String(note).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  childProcess.execSync("echo " + cohort);
  res.json({ accepted: true });
}
