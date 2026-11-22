// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const normalizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const dossier: string = parts.join(',');
  childProcess.spawn("echo " + dossier, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
