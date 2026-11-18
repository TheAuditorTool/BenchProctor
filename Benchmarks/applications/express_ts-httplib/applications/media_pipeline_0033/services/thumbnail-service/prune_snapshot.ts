// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneSnapshot = async (req: Request, res: Response): Promise<void> => {
  const transcript = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const rendition: string = normalize(transcript);
  const resolved = path.resolve("/var/app/data", rendition);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const montage = resolved;
  fs.writeFileSync(montage, "data");
  res.json({ accepted: true });
}
