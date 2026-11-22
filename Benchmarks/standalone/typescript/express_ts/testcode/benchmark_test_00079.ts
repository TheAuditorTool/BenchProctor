// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00079 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const data = `${userInput}`;
  if (!["ls", "cat", "date", "whoami"].includes(data)) { res.status(403).json({error:'forbidden'}); return; }
  const allowedBin = data;
  childProcess.exec("echo " + allowedBin, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
