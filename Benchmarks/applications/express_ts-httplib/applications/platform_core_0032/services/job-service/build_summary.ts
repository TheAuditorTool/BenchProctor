// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const buildSummary = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const persona: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  childProcess.exec("echo " + handshake, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
