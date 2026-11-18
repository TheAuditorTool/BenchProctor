// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00390 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  res.json({ accepted: true });
}
