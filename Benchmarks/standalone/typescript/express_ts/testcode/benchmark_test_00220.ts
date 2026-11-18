// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00220 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  childProcess.execFileSync("echo", [userInput]);
  res.json({ accepted: true });
}
