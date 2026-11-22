// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const pruneCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const rendition: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(rendition)) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  childProcess.exec("echo " + montage, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
