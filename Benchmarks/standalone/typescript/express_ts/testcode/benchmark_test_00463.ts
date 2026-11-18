// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00463 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  res.json({ accepted: true });
}
