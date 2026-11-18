// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolveDigest = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const grievance: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(grievance)) { res.status(400).json({error:"invalid"}); return; }
  const verdict = grievance;
  childProcess.execSync("echo " + verdict);
  res.json({ accepted: true });
}
