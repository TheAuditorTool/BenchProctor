// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectMetric = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(paragraph).split(',')) { parts.push(token); }
  const gauge: string = parts.join(',');
  childProcess.execFileSync("echo", [gauge]);
  res.json({ accepted: true });
}
