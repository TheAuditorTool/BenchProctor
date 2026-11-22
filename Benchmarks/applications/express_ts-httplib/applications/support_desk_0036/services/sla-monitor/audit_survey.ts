// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditSurvey = async (req: Request, res: Response): Promise<void> => {
  const preface = process.env.SUPPORT_INPUT_0036 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const grievance: string = normalize(preface);
  childProcess.spawn("echo " + grievance, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
