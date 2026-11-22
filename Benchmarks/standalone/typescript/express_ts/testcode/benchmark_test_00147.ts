// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00147 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.exec("echo " + data, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
