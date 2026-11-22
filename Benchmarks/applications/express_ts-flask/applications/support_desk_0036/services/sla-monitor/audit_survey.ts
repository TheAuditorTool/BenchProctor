// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditSurvey = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body?.payload as string) || "";
  const grievance = preface != null ? preface : '';
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
