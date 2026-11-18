// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const verifyConversion = async (req: Request, res: Response): Promise<void> => {
  const note = (req.query.id as string) || "";
  const [addendum] = String(note).split(',');
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const dossier = addendum;
  childProcess.execSync("echo " + dossier);
  res.json({ accepted: true });
}
