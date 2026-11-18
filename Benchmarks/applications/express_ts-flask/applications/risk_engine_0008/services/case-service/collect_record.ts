// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const collectRecord = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body.payload as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const verdict: string = normalize(synopsis);
  if (!/^(asc|desc|name|created)$/.test(String(verdict))) { res.status(400).json({error:"invalid"}); return; }
  const grievance = verdict;
  childProcess.execSync("echo " + grievance);
  res.json({ accepted: true });
}
