// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const normalizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(transcript);
  const heading: string = readInput();
  const resolved = path.resolve("/var/app/data", heading);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const passage = resolved;
  fs.unlinkSync(passage);
  res.json({ accepted: true });
}
