// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateProfile = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(preface);
  const grievance: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(grievance)) { res.status(403).json({error:'forbidden'}); return; }
  const inquiry = grievance;
  childProcess.execSync("echo " + inquiry);
  res.json({ accepted: true });
}
