// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const mergeReceipt = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const rendition: string = parts.join(',');
  childProcess.execSync("echo " + rendition);
  res.json({ accepted: true });
}
