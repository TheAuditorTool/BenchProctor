// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const auditManifest = async (req: Request, res: Response): Promise<void> => {
  const tagline = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(tagline);
  const resolved = path.resolve("/var/app/data", persona);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const handshake = resolved;
  fs.writeFileSync(handshake, "data");
  res.json({ accepted: true });
}
