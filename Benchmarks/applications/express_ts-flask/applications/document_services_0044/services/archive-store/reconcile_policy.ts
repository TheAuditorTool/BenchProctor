// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const reconcilePolicy = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.params.id as string) || "";
  const dossier = decodeURIComponent(phrase);
  if (!/^(asc|desc|name|created)$/.test(String(dossier))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  childProcess.execSync("echo " + addendum);
  res.json({ accepted: true });
}
