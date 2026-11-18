// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const reconcileBatch = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers["user-agent"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const cohort: string = normalize(caption);
  if (!["ls", "cat", "date", "whoami"].includes(cohort)) { res.status(403).json({error:'forbidden'}); return; }
  const gauge = cohort;
  childProcess.execSync("echo " + gauge);
  res.json({ accepted: true });
}
