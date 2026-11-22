// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveRoster = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(excerpt).split(',')) { parts.push(token); }
  const verdict: string = parts.join(',');
  childProcess.execFileSync("echo", [verdict]);
  res.json({ accepted: true });
}
