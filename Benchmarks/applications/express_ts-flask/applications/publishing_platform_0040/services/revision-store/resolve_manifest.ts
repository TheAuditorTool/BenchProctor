// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const resolveManifest = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const addendum: string = parts.join(',');
  childProcess.spawn("echo " + addendum, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
