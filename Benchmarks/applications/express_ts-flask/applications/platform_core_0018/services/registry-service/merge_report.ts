// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const mergeReport = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(subtitle).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  childProcess.spawn("echo " + persona, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
