// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const validateHeader = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(notice).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  childProcess.execFileSync("echo", [backorder]);
  res.json({ accepted: true });
}
