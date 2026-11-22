// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeConfig = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(heading);
  const addendum: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(addendum)) { res.status(400).json({error:"invalid"}); return; }
  const byline = addendum;
  childProcess.spawn("echo " + byline, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
