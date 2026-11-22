// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const exportDigest = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body.field as string) || "";
  const parts: string[] = [];
  for (const token of String(wording).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  childProcess.execFileSync("echo", [backorder]);
  res.json({ accepted: true });
}
