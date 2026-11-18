// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const verifyDevice = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(phrase);
  const persona: string = readInput();
  const resolved = path.resolve("/var/app/data", persona);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const transcript = resolved;
  fs.unlinkSync(transcript);
  res.json({ accepted: true });
}
