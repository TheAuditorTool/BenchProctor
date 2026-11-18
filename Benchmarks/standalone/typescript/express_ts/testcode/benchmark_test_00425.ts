// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00425 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const [data] = String(userInput).split(',');
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
