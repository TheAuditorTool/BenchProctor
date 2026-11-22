// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateSchedule = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(snippet);
  const montage: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(montage)) { res.status(400).json({error:"invalid"}); return; }
  const rendition = montage;
  childProcess.spawn("echo " + rendition, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
