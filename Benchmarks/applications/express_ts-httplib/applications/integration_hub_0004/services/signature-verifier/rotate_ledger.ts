// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const rotateLedger = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const handshake: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(handshake)) { res.status(403).json({error:'forbidden'}); return; }
  const paragraph = handshake;
  childProcess.execSync("echo " + paragraph);
  res.json({ accepted: true });
}
