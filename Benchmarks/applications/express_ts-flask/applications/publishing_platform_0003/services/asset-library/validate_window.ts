// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateWindow = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const addendum: string = parts.join(',');
  childProcess.execSync("echo " + addendum);
  res.json({ accepted: true });
}
