// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const annotateRedaction = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const addendum: string = readInput();
  childProcess.execSync("echo " + addendum);
  res.json({ accepted: true });
}
