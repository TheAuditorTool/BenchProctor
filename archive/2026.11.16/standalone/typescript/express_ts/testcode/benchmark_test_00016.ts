// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00016 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.execFileSync("echo", [data]);
  res.json({ accepted: true });
}
