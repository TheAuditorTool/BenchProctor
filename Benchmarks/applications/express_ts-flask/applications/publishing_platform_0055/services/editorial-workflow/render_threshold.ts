// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const renderThreshold = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(synopsis);
  const byline: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(byline)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  childProcess.spawn("echo " + addendum, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
