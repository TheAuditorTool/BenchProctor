// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const publishCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(preface);
  const bulletin: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const citation = bulletin;
  childProcess.exec("echo " + citation, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
