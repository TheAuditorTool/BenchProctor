// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadCaption = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const rendition: string = parts.join(',');
  childProcess.execSync("echo " + rendition);
  res.json({ accepted: true });
}
