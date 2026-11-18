// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const publishConfig = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const remark: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(remark)) { res.status(403).json({error:'forbidden'}); return; }
  const wording = remark;
  childProcess.execSync("echo " + wording);
  res.json({ accepted: true });
}
