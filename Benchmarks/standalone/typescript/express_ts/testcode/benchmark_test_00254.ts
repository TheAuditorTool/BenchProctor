// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const BenchmarkTest00254 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  res.json({ accepted: true });
}
