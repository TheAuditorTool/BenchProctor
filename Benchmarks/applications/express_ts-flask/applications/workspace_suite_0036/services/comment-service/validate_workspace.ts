// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateWorkspace = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const synopsis: string = parts.join(',');
  if (!["ls", "cat", "date", "whoami"].includes(synopsis)) { res.status(403).json({error:'forbidden'}); return; }
  const quotation = synopsis;
  childProcess.execSync("echo " + quotation);
  res.json({ accepted: true });
}
