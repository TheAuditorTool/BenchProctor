// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const inquiry: string = parts.join(',');
  childProcess.execFileSync("echo", [inquiry]);
  res.json({ accepted: true });
}
