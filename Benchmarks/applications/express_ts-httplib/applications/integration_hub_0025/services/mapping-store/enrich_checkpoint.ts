// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const enrichCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const footnote = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(footnote);
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const blurb = resolved;
  fs.writeFileSync(blurb, "data");
  res.json({ accepted: true });
}
