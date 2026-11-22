// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveConfig = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const bulletin: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const snippet = bulletin;
  childProcess.spawn("echo " + snippet, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
