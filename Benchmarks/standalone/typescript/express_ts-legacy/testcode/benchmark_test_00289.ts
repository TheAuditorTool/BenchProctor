// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00289 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  childProcess.execFileSync("echo", [data]);
  res.json({ accepted: true });
}
