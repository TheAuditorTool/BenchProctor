// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00289 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const [data] = String(userInput).split(',');
  childProcess.execFileSync("echo", [data]);
  res.json({ accepted: true });
}
