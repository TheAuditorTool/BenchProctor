// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const fetchThreshold = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body?.field as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const dossier: string = parts.join(',');
  childProcess.execFileSync("echo", [dossier]);
  res.json({ accepted: true });
}
