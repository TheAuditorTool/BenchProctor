// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as nodeUtil from "util";

export const BenchmarkTest00024 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
