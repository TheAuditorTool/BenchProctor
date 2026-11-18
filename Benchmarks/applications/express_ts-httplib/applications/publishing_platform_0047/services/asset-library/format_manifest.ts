// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const formatManifest = async (req: Request, res: Response): Promise<void> => {
  const synopsis = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const byline: string = normalize(synopsis);
  const resolved = path.resolve("/var/app/data", byline);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const addendum = resolved;
  fs.writeFileSync(addendum, "data");
  res.json({ accepted: true });
}
