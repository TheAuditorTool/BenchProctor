// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const publishSignature = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const dossier: string = transform(excerpt);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(dossier)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  childProcess.execSync("echo " + addendum);
  res.json({ accepted: true });
}
