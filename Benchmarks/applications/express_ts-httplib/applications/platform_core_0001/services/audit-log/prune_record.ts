// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const pruneRecord = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(tagline);
  const persona: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
