// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const loadManifest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.payload as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(note);
  if (!/^(asc|desc|name|created)$/.test(String(gauge))) { res.status(400).json({error:"invalid"}); return; }
  const cohort = gauge;
  childProcess.execSync("echo " + cohort);
  res.json({ accepted: true });
}
