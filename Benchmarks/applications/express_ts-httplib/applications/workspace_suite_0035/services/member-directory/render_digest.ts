// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderDigest = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(paragraph);
  const wording: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(wording)) { res.status(403).json({error:'forbidden'}); return; }
  const transcript = wording;
  childProcess.execSync("echo " + transcript);
  res.json({ accepted: true });
}
