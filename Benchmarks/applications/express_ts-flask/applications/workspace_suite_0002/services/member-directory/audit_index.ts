// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const auditIndex = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body.field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(transcript);
  const heading: string = readInput();
  childProcess.execSync("echo " + heading);
  res.json({ accepted: true });
}
