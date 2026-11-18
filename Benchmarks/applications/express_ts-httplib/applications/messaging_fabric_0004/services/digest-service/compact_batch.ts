// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactBatch = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(paragraph);
  const bulletin: string = readInput();
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = bulletin;
  childProcess.execSync("echo " + synopsis);
  res.json({ accepted: true });
}
