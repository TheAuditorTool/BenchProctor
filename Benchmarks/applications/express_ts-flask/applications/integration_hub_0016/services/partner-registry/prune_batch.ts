// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const pruneBatch = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(wording);
  const handshake: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const subject = handshake;
  childProcess.spawn("echo " + subject, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
