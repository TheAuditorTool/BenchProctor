// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00334 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const data: string = normalize(userInput);
  if (!["ls", "cat", "date", "whoami"].includes(data)) { res.status(403).json({error:'forbidden'}); return; }
  const allowedBin = data;
  childProcess.spawn("echo " + allowedBin, { shell: true, stdio: "inherit" });
  res.json({ accepted: true });
}
