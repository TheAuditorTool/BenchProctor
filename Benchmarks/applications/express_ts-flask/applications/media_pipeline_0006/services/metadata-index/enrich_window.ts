// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichWindow = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.field as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(passage);
  const montage: string = readInput();
  childProcess.execSync("echo " + montage);
  res.json({ accepted: true });
}
