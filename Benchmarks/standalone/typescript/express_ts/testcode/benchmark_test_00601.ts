// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00601 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = decodeURIComponent(userInput);
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
