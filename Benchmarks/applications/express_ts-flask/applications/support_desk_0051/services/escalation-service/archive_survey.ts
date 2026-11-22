// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveSurvey = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(preface);
  const grievance: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(grievance)) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  childProcess.spawn("echo " + inquiry, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
