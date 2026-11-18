// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const renderIndex = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const addendum: string = normalize(summary);
  const resolved = path.resolve("/var/app/data", addendum);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const byline = resolved;
  fs.writeFileSync(byline, "data");
  res.json({ accepted: true });
}
