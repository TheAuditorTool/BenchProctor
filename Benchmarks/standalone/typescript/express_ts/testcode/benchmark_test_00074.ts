// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00074 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.payload as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  if (!["ls", "cat", "date", "whoami"].includes(data)) { res.status(403).json({error:'forbidden'}); return; }
  const allowedBin = data;
  childProcess.exec("echo " + allowedBin, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
