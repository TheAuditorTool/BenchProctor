// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadPolicy = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const phrase: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(phrase)) { res.status(400).json({error:"invalid"}); return; }
  const subtitle = phrase;
  childProcess.spawn("echo " + subtitle, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
