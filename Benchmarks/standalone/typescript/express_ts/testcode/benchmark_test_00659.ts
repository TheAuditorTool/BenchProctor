// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00659 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
