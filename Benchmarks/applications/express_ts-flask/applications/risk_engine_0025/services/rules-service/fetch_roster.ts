// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.params.id as string) || "";
  const verdict = decodeURIComponent(excerpt);
  if (!/^(asc|desc|name|created)$/.test(String(verdict))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = verdict;
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
