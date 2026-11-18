// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const summarizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const bulletin: string = readInput();
  childProcess.execSync("echo " + bulletin);
  res.json({ accepted: true });
}
