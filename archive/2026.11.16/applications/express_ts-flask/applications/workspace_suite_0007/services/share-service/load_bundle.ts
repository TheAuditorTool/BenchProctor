// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadBundle = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const subtitle: string = transform(summary);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(subtitle)) { res.status(400).json({error:"invalid"}); return; }
  const notice = subtitle;
  childProcess.execSync("echo " + notice);
  res.json({ accepted: true });
}
