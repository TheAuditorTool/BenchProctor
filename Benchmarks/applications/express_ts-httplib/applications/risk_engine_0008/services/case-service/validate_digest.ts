// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const validateDigest = async (req: Request, res: Response): Promise<void> => {
  const synopsis = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const verdict: string = normalize(synopsis);
  const resolved = path.resolve("/var/app/data", verdict);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const grievance = resolved;
  fs.writeFileSync(grievance, "data");
  res.json({ accepted: true });
}
