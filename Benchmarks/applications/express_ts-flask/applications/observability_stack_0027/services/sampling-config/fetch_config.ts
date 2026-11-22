// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchConfig = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
