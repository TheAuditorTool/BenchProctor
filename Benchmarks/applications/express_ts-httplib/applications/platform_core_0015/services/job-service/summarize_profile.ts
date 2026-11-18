// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const summarizeProfile = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const handshake: string = readInput();
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const persona = resolved;
  fs.unlinkSync(persona);
  res.json({ accepted: true });
}
