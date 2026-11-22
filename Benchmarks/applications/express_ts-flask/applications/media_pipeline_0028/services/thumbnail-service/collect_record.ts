// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectRecord = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.field as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const rendition: string = parts.join(',');
  childProcess.execFileSync("echo", [rendition]);
  res.json({ accepted: true });
}
