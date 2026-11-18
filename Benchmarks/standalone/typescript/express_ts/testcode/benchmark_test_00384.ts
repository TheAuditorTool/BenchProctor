// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00384 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = Buffer.from(userInput, "hex").toString();
  childProcess.execSync("echo " + data);
  res.json({ accepted: true });
}
