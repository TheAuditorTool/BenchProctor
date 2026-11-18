// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00343 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!["ls", "cat", "date", "whoami"].includes(data)) { res.status(403).json({error:'forbidden'}); return; }
  const allowedBin = data;
  childProcess.execSync("echo " + allowedBin);
  res.json({ accepted: true });
}
