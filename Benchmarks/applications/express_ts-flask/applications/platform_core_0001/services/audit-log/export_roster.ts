// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const exportRoster = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body.field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(tagline);
  const persona: string = readInput();
  childProcess.execSync("echo " + persona);
  res.json({ accepted: true });
}
