// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00409 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = decodeURIComponent(userInput);
  childProcess.execFileSync("echo", [data]);
  res.json({ accepted: true });
}
