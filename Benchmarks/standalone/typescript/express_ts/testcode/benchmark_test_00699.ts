// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00699 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
