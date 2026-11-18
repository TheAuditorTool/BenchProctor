// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichConfig = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.query.id as string) || "";
  const [gauge] = String(excerpt).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(gauge)) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  childProcess.execSync("echo " + cohort);
  res.json({ accepted: true });
}
