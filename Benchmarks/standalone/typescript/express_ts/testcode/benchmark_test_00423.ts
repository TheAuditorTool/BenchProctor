// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00423 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const parts: string[] = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data: string = parts.join(',');
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
