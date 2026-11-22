// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const mergeReport = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const remittance: string = parts.join(',');
  childProcess.execSync("echo " + remittance);
  res.json({ accepted: true });
}
