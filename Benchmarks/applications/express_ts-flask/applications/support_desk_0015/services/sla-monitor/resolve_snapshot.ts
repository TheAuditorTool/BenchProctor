// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolveSnapshot = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(phrase).split(',')) { parts.push(token); }
  const grievance: string = parts.join(',');
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
