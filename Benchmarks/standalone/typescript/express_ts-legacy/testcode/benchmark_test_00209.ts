// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as nodeUtil from "util";

export const BenchmarkTest00209 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.exec("echo " + data, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
