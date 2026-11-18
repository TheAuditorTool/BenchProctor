// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const note = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(note);
  const resolved = path.resolve("/var/app/data", gauge);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const cohort = resolved;
  fs.writeFileSync(cohort, "data");
  res.json({ accepted: true });
}
