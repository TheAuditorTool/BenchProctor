// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectRecord = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(synopsis);
  const verdict: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(verdict)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = verdict;
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
