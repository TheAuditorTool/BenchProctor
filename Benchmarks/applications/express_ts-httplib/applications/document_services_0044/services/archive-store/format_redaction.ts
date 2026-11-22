// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const formatRedaction = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(phrase);
  const dossier: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(dossier)) { res.status(403).json({error:'forbidden'}); return; }
  const addendum = dossier;
  childProcess.execSync("echo " + addendum);
  res.json({ accepted: true });
}
