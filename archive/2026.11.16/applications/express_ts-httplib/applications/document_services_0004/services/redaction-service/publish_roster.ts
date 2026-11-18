// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const publishRoster = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(excerpt).split(',')) { parts.push(token); }
  const dossier: string = parts.join(',');
  childProcess.execSync("echo " + dossier);
  res.json({ accepted: true });
}
