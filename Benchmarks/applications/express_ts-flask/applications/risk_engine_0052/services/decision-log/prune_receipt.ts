// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const pruneReceipt = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(memo).split(',')) { parts.push(token); }
  const verdict: string = parts.join(',');
  childProcess.execFileSync("echo", [verdict]);
  res.json({ accepted: true });
}
