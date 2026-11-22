// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00245 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
