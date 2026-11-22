// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00107 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.authorization as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
