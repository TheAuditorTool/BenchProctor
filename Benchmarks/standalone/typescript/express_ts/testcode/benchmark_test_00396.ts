// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as nodeUtil from "util";

export const BenchmarkTest00396 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
