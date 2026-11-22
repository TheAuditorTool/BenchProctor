// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeConfig = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const byline: string = parts.join(',');
  childProcess.execFileSync("echo", [byline]);
  res.json({ accepted: true });
}
