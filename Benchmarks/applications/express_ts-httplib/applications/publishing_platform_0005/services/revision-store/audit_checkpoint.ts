// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const auditCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const byline: string = readInput();
  const resolved = path.resolve("/var/app/data", byline);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const addendum = resolved;
  fs.unlinkSync(addendum);
  res.json({ accepted: true });
}
