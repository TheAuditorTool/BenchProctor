// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const mergeReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const persona: string = readInput();
  if (!["ls", "cat", "date", "whoami"].includes(persona)) { res.status(403).json({error:'forbidden'}); return; }
  const handshake = persona;
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
