// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00209 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.field as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
