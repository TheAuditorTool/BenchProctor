// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as nodeUtil from "util";

export const BenchmarkTest00015 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
