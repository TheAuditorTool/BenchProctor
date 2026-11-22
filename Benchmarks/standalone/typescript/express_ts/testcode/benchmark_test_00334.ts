// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00334 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
